import tkinter as tk
import math as m
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def convert_to_float(s):
    if 'e' in s:
        base, exponent = s.split('e')
        return float(base) * 10 ** int(exponent)
    else:
        return float(s)

########################################################################################
#Defines the physics formula to be simulated
def calculate_S():
    N = int(N_entry.get())
    n = int(n_entry.get())
    k = 1.380649e-23
    omega = m.factorial(N) / (m.factorial(n) * m.factorial(N - n))
    S = k * m.log(omega)
    output_label.config(text=f"Ω = {omega}\nS = {S}")

########################################################################################
#Create the graphical component
def create_graph():
    N = int(N_entry.get())
    n = int(n_entry.get())

    # Remove existing graph if there is one
    if hasattr(window, 'graph_canvas'):
        window.graph_canvas.get_tk_widget().pack_forget()
        window.graph_canvas.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    dipoles = np.arange(N)
    down_arrows = np.random.choice(dipoles, N - n, replace=False)

#Draws the up and down arrows according to the input values
    for i in dipoles:
        if i in down_arrows:
            arrow = patches.Arrow(i + 1, 0, 0, -1, width=N * 0.05, color='black')
        else:
            arrow = patches.Arrow(i + 1, 0, 0, 1, width=N * 0.05, color='black')
        ax.add_patch(arrow)
########################################################################################

#Get rid of the x and y axis ticks as its not really meaningful
    ax.set_xticks([])
    ax.set_yticks([])
    plt.ylabel('Upwards Facing Field')
#The xlim values scale to the number of arrows (N values). This prevents over clutter 
#and keeps the arrows within the graph
    plt.xlim(0, N + 1)
    plt.ylim(-2, 2)

    # Create a canvas to display the graph
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # Add the canvas to the window
    canvas.get_tk_widget().pack()

    # Store the canvas object in the window object
    window.graph_canvas = canvas

########################################################################################
#This is the code for the 'application' element of the simulation. 
#ie. the text input, buttons and resultant values.
window = tk.Tk()
window.title("Calculate S")

#text entry for N values 
N_label = tk.Label(window, text="Enter the value of N:")
N_label.pack()
N_entry = tk.Entry(window)
N_entry.pack()

#text entry for n values 
n_label = tk.Label(window, text="Enter the value of n:")
n_label.pack()
n_entry = tk.Entry(window)
n_entry.pack()

#create graph button
graph_button = tk.Button(window, text="Create Graph", command=create_graph)
graph_button.pack()

#calculate numerical results button 
calculate_button = tk.Button(window, text="Calculate S", command=calculate_S)
calculate_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
