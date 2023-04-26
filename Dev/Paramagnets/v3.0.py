import tkinter as tk
import math as m
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


# Convert exponential notation to a float value
# eg.  5e6 becomes 5*10**6
def convert_to_float(s):
    if 'e' in s:
        base, exponent = s.split('e')
        return float(base) * 10 ** int(exponent)
    else:
        return float(s)


def create_graph():
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

    ##########################################################
    # Define a number N dipoles and n poles aligned with the field
    N = 6
    n = 2
    ##########################################################

    dipoles = np.arange(N)  # Create an array of integers from 0 to N-1

    # Generate a random sample of 'n' integers between 0 and N-1
    down_arrows = np.random.choice(dipoles, N - n, replace=False)

    # Plot the arrows
    for i in dipoles:
        if i in down_arrows:  # If the arrow should face down
            arrow = patches.Arrow(i + 1, 0, 0, -1, width=N * 0.05, color='black')
        else:  # If the arrow should face up
            arrow = patches.Arrow(i + 1, 0, 0, 1, width=N * 0.05, color='black')
        ax.add_patch(arrow)

    # Set the axis limits
    plt.xlim(0, N + 1)
    plt.ylim(-2, 2)
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

# Create a label and entry field for omega
#N_label = tk.Label(window, text="Enter the value of N:")
#N_label.pack()
#N_entry = tk.Entry(window)
#N_entry.pack()

# Create a label and entry field for omega
#n_label = tk.Label(window, text="Enter the value of n:")
#n_label.pack()
#n_entry = tk.Entry(window)
#n_entry.pack()

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
