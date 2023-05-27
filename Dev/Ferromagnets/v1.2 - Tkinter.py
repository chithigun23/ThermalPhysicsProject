import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import FancyArrow
import numpy as np
import os
import sys
import subprocess

def FerroPlot():
    global Bx_entry, By_entry

    Bx = Bx_entry.get()
    By = By_entry.get()

    if not Bx:
        Bx = 0.0
    else:
        Bx = float(Bx)

    if not By:
        By = 0.0
    else:
        By = float(By)

    u = u_initial + Bx
    v = v_initial + By

    ax.clear()

    for i in range(n):
        for j in range(n):
            arrow = FancyArrow(j, i, u[i, j], v[i, j], color='k', width=0.01)
            ax.add_patch(arrow)

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Ferromagnetism Simulation with Applied Magnetic Field')

    canvas.draw()

    dirArrow(Bx, By)

def dirArrow(Bx, By):
    small_ax.clear()

    magnitude = np.sqrt(Bx**2 + By**2)
    if magnitude != 0:
        Bx /= magnitude
        By /= magnitude

    small_ax.arrow(0.5, 0.5, Bx*0.4, By*0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')

    small_ax.set_xlim(0, 1)
    small_ax.set_ylim(0, 1)
    small_ax.set_xlabel('Bx')
    small_ax.set_ylabel('By')
    small_ax.set_title('Applied Magnetic Field')

    small_canvas.draw()

window = tk.Tk()
window.title("Ferromagnetism Simulation")

fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)

n = 40

u_initial = np.ones((n, n))
v_initial = np.zeros((n, n))

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

for zone in zones:
    u_initial[zone["rows"], zone["cols"]] = np.cos(zone["angle"])
    v_initial[zone["rows"], zone["cols"]] = np.sin(zone["angle"])

Bx = 0.5
By = 0.5

u = u_initial + Bx
v = v_initial + By

for i in range(n):
    for j in range(n):
        arrow = FancyArrow(j, i, u[i, j], v[i, j], color='k', width=0.01)
        ax.add_patch(arrow)

ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ferromagnetism Simulation with Applied Magnetic Field')

plot_frame = tk.Frame(window)
plot_frame.pack(side='left')

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack()

small_fig = Figure(figsize=(3, 3), dpi=100)
small_ax = small_fig.add_subplot(111)
small_canvas = FigureCanvasTkAgg(small_fig, master=plot_frame)
small_canvas.draw()
small_canvas.get_tk_widget().pack()

Bx_frame = tk.Frame(window)
Bx_frame.pack(anchor='w')

Bx_label = tk.Label(Bx_frame, text="Bx:")
Bx_label.pack(side='left')
Bx_entry = tk.Entry(Bx_frame)
Bx_entry.pack(side='left')

By_frame = tk.Frame(window)
By_frame.pack(anchor='w')

By_label = tk.Label(By_frame, text="By:")
By_label.pack(side='left')
By_entry = tk.Entry(By_frame)
By_entry.pack(side='left')

calculate_button = tk.Button(window, text="Calculate", command=FerroPlot)
calculate_button.pack()

def back_to_menu():
    window.destroy()
    menu_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MENU', 'menu.py')
    subprocess.Popen([sys.executable, menu_script_path])

back_button = tk.Button(window, text="Back", command=back_to_menu)
back_button.pack()

window.mainloop()
