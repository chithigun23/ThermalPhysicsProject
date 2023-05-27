import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess
from tkinter import *
import os
import sys

def plot_large_dots(n,d, frame):
    # Clear previous figures
    for widget in frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots()

    # Generate the y-coordinates for the large dots
    y_coords = np.arange(0, n*d,d)

    # Plot the large dots as scatter points
    ax.scatter(np.zeros_like(y_coords), y_coords, s=100, color='black')

    # Hide the x-axis ticks and show relevant yaxis ticks
    ax.set_xticks([])
    ax.set_yticks(np.arange(0,n*d,d))

    # Set the y-axis limits
    ax.set_ylim(-1, n*d + 1)

    # Set labels and title
    ax.set_xlabel('Energy')
    ax.set_ylabel('')
    ax.set_title('Ground-state Fermi energy')

    # Calculate the energy sum
    energy_sum = np.sum(y_coords)

    # Add text onto the plot
    ax.text(0.037, n*d-(d/2), 'E=' + str(energy_sum), fontsize=12, color='red',  bbox=dict(facecolor='black', alpha=0.15))

    # Show plot
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def calculate():
    num_large_dots = int(num_large_dots_entry.get())
    diff = float(diff_entry.get())
    plot_large_dots(num_large_dots, diff, plot_frame)

root = Tk()
root.title("Fermi Energy Calculation")

# Create labels and entries for user input
num_large_dots_label = Label(root, text="Number of Large Dots (Positive Integer)")
num_large_dots_label.pack()
num_large_dots_entry = Entry(root)
num_large_dots_entry.pack()

diff_label = Label(root, text="Difference (Real Number)")
diff_label.pack()
diff_entry = Entry(root)
diff_entry.pack()

calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create a frame for the plot
plot_frame = Frame(root)
plot_frame.pack()

def back_to_menu():
    # This will destroy the current window
    root.destroy()
    # This will run the menu script
    menu_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MENU', 'menu.py')
    subprocess.Popen([sys.executable, menu_script_path])

# Create a Back button
back_button = Button(root, text="Back", command=back_to_menu)
back_button.pack()

root.mainloop()
