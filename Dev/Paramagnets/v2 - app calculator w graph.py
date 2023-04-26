import tkinter as tk
import math as m
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Convert exponential notation to a float value
#eg.  5e6 becomes 5*10**6
def convert_to_float(s):
    if 'e' in s:
        base, exponent = s.split('e')
        return float(base) * 10 ** int(exponent)
    else:
        return float(s)
    
    
    
def create_graph():
    # Create the figure and axis objects
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Create the data to plot
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]

    # Plot the data
    ax.plot(x_values, y_values)

    # Add labels to the plot
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Graph')

    # Create a canvas to display the graph
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # Add the canvas to the window
    canvas.get_tk_widget().pack()
    
    

# Define a function to calculate the value of S
def calculate_S():
    # Get the value of omega from the input field
    omega_str = omega_entry.get()

    # Convert the input string to a float value, accounting for exponential notation
    omega = convert_to_float(omega_str.replace("*10^", "e"))

    # Set the value of k
    k = 1.380649e-23

    # Calculate S using equation S=k∙ln(Ω)
    S = k * m.log(omega)

    # Display the result in the output label
    output_label.config(text=f"S = {S}")
    
# Create a GUI window
window = tk.Tk()
window.title("Calculate S")

# Create a label and entry field for omega
omega_label = tk.Label(window, text="Enter the value of omega:")
omega_label.pack()
omega_entry = tk.Entry(window)
omega_entry.pack()

# Add a button to create the graph
graph_button = tk.Button(window, text="Create Graph", command=create_graph)
graph_button.pack()

# Create a button to calculate S
calculate_button = tk.Button(window, text="Calculate S", command=calculate_S)
calculate_button.pack()

# Create a label for the output
output_label = tk.Label(window, text="")
output_label.pack()

# Start the GUI event loop
window.mainloop()
