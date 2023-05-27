import tkinter as tk
import math as m
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.patches as patches
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import subprocess
import sys

def convert_to_float(s):
    if 'e' in s:
        base, exponent = s.split('e')
        return float(base) * 10 ** int(exponent)
    else:
        return float(s)

def calculate_S():
    try:
        N = int(N_entry.get())
        n = int(n_entry.get())
        if N < 0 or n < 0:
            raise ValueError("Dipole values must be non-negative.")
        if n > N:
            raise ValueError("'n' cannot be greater than 'N'.")
    except ValueError:
        error_label.config(text="Invalid input. Please enter non-negative integers only.")
        return
    error_label.config(text="")
    k = 1.380649e-23
    omega = m.factorial(N) / (m.factorial(n) * m.factorial(N - n))
    S = k * m.log(omega)
    output_label.config(text=f"Ω = {omega}\nS = {S}")

def create_graph():
    try:
        N = int(N_entry.get())
        n = int(n_entry.get())
        if N < 0 or n < 0:
            raise ValueError("Dipole values must be non-negative.")
        if n > N:
            raise ValueError("'n' cannot be greater than 'N'.")
    except ValueError:
        error_label.config(text="Invalid input. Please enter non-negative integers only.")
        return
    error_label.config(text="")
    a = (-(2)*n) + N
    theta = np.linspace(0, np.pi, 100)
    x = N * np.cos(theta)
    y = N * np.sin(theta)
    x_a = a
    y_a = np.sqrt(N**2 - (x_a)**2)

    if hasattr(window, 'graph_canvas'):
        window.graph_canvas.get_tk_widget().pack_forget()
        window.graph_canvas.get_tk_widget().destroy()

    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    dipoles = np.arange(N)
    down_arrows = np.random.choice(dipoles, N - n, replace=False)
    for i in dipoles:
        if i in down_arrows:
            arrow = patches.Arrow(i + 1, 0, 0, -1, width=N * 0.05, color='black')
        else:
            arrow = patches.Arrow(i + 1, 0, 0, 1, width=N * 0.05, color='black')
        ax.add_patch(arrow)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylabel('Upwards Facing Field')
    ax.set_xlim(0, N + 1)
    ax.set_ylim(-2, 2)

    ax2.plot(x, y, 'b', linewidth=2)
    ax2.plot(x_a, y_a, 'ro')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.axis('equal')
    x_intercepts = [-N, N, 0]
    ax2.set_xticks(x_intercepts)
    ax2.set_yticks([])
    ax2.set_ylim(0, N + 0.1)
    ax2.set_xlabel('Internal Energy ($U/μB$)', fontsize=12)
    ax2.set_ylabel('Entropy ($S/k$)', fontsize=12)
    ax2.set_title('Temperature Plot', fontsize=14)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.graph_canvas = canvas

def on_enter_key(event):
    create_graph()

window = tk.Tk()
window.title("Paramagnet Calculator")

N_label = tk.Label(window, text="Number of Total Dipoles (N):")
N_label.pack()
N_entry = tk.Entry(window)
N_entry.pack()
N_entry.bind("<Return>", on_enter_key)

n_label = tk.Label(window, text="Number of dipoles aligned (n):")
n_label.pack()
n_entry = tk.Entry(window)
n_entry.pack()
n_entry.bind("<Return>", on_enter_key)

graph_button = tk.Button(window, text="Create Graph", command=create_graph)
graph_button.pack()

calculate_button = tk.Button(window, text="Calculate S", command=calculate_S)
calculate_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

error_label = tk.Label(window, text="", fg="red")  # label for error messages
error_label.pack()

def back_to_menu():
    window.destroy()
    menu_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MENU', 'menu.py')
    subprocess.Popen([sys.executable, menu_script_path])

back_button = tk.Button(window, text="Back", command=back_to_menu)
back_button.pack()

window.mainloop()
