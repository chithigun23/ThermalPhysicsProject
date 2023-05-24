import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import FancyArrow
import numpy as np

def FerroPlot():
    global Bx_entry, By_entry

    # Get the Bx and By values from the entry fields
    Bx = Bx_entry.get()
    By = By_entry.get()

    # Check if the fields are empty
    if not Bx:
        Bx = 0.0  # default value, can be adjusted
    else:
        Bx = float(Bx)

    if not By:
        By = 0.0  # default value, can be adjusted
    else:
        By = float(By)

    # Update the arrow directions based on the applied field
    u = u_initial + Bx
    v = v_initial + By

    # Clear the previous plot
    ax.clear()

    # Plot the arrows
    for i in range(n):
        for j in range(n):
            arrow = FancyArrow(j, i, u[i, j], v[i, j], color='k', width=0.01)
            ax.add_patch(arrow)

    # Set the limits and labels
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Ferromagnetism Simulation with Applied Magnetic Field')

    # Redraw the plot
    canvas.draw()

    # Update the small plot with the magnetic field direction
    dirArrow(Bx, By)

def dirArrow(Bx, By):
    # Clear the previous plot
    small_ax.clear()

    # Normalize the Bx and By values for consistent arrow size
    magnitude = np.sqrt(Bx**2 + By**2)
    if magnitude != 0:  # Avoid division by zero
        Bx /= magnitude
        By /= magnitude

    # Draw an arrow
    small_ax.arrow(0.5, 0.5, Bx*0.4, By*0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')

    # Set the limits and labels
    small_ax.set_xlim(0, 1)
    small_ax.set_ylim(0, 1)
    small_ax.set_xlabel('Bx')
    small_ax.set_ylabel('By')
    small_ax.set_title('Applied Magnetic Field')

    # Redraw the plot
    small_canvas.draw()

# Create the Tkinter window
window = tk.Tk()
window.title("Ferromagnetism Simulation")

# Create the Figure and Axes for the plot
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)

# Define the size of the grid
n = 40

# Initialize the directions of the arrows to simulate ferromagnetism
u_initial = np.ones((n, n))
v_initial = np.zeros((n, n))

# Define the ferromagnetic domains
zones = [
    {"rows": slice(0, n//3), "cols": slice(0, n//3), "angle": 0},
    {"rows": slice(0, n//3), "cols": slice(n//3, 2*n//3), "angle": np.pi/4},
    {"rows": slice(0, n//3), "cols": slice(2*n//3, n), "angle": np.pi/2},
    {"rows": slice(n//3, 2*n//3), "cols": slice(0, n//3), "angle": 3*np.pi/4},
    {"rows": slice(n//3, 2*n//3), "cols": slice(n//3, 2*n//3), "angle": np.pi/6},
    {"rows": slice(n//3, 2*n//3), "cols": slice(2*n//3, n), "angle": 5*np.pi/6},
    {"rows": slice(2*n//3, n), "cols": slice(0, n//3), "angle": np.pi},
    {"rows": slice(2*n//3, n), "cols": slice(n//3, 2*n//3), "angle": -np.pi/4},
    {"rows": slice(2*n//3, n), "cols": slice(2*n//3, n), "angle": -np.pi/2},
]

# Adjust the direction of the arrows based on the zones
for zone in zones:
    u_initial[zone["rows"], zone["cols"]] = np.cos(zone["angle"])
    v_initial[zone["rows"], zone["cols"]] = np.sin(zone["angle"])

# Define the applied magnetic field (x and y components)
Bx = 0.5  # Initial magnitude of the field in the x-direction
By = 0.5  # Initial magnitude of the field in the y-direction

# Update the arrow directions based on the applied field
u = u_initial + Bx
v = v_initial + By

# Plot the arrows
for i in range(n):
    for j in range(n):
        arrow = FancyArrow(j, i, u[i, j], v[i, j], color='k', width=0.01)
        ax.add_patch(arrow)

# Set the limits and labels
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ferromagnetism Simulation with Applied Magnetic Field')

# Create a frame for the main plot and small plot
plot_frame = tk.Frame(window)
plot_frame.pack(side='left')

# Create the FigureCanvasTkAgg widget for main plot
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Add small plot
small_fig = Figure(figsize=(3, 3), dpi=100)
small_ax = small_fig.add_subplot(111)
small_canvas = FigureCanvasTkAgg(small_fig, master=plot_frame)
small_canvas.draw()
small_canvas.get_tk_widget().pack()

# Create the Bx frame
Bx_frame = tk.Frame(window)
Bx_frame.pack(anchor='w')

# Create the Bx entry field and label inside Bx frame
Bx_label = tk.Label(Bx_frame, text="Bx:")
Bx_label.pack(side='left')
Bx_entry = tk.Entry(Bx_frame)
Bx_entry.pack(side='left')

# Create the By frame
By_frame = tk.Frame(window)
By_frame.pack(anchor='w')

# Create the By entry field and label inside By frame
By_label = tk.Label(By_frame, text="By:")
By_label.pack(side='left')
By_entry = tk.Entry(By_frame)
By_entry.pack(side='left')

# Create the Calculate button
calculate_button = tk.Button(window, text="Calculate", command=FerroPlot)
calculate_button.pack()

# Start the Tkinter event loop
tk.mainloop()
