import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
from ipywidgets import interact

# Define the size of the grid
n = 20

# Initialize the grid
x, y = np.meshgrid(np.arange(n), np.arange(n))

# Initialize the directions of the arrows to simulate ferromagnetism
u = np.ones((n, n))
v = np.zeros((n, n))

# Define the zones for the ferromagnetic domains
zones = [
    {"rows": slice(0, n//4), "cols": slice(0, n//2), "angle": 0},
    {"rows": slice(0, n//4), "cols": slice(n//2, n), "angle": np.pi/4},
    {"rows": slice(n//4, n//2), "cols": slice(0, n//2), "angle": np.pi/2},
    {"rows": slice(n//4, n//2), "cols": slice(n//2, n), "angle": 3*np.pi/4},
    {"rows": slice(n//2, 3*n//4), "cols": slice(0, n//2), "angle": np.pi},
    {"rows": slice(n//2, 3*n//4), "cols": slice(n//2, n), "angle": 5*np.pi/4},
    {"rows": slice(3*n//4, n), "cols": slice(0, n//2), "angle": 3*np.pi/2},
    {"rows": slice(3*n//4, n), "cols": slice(n//2, n), "angle": 7*np.pi/4},
]

def plot_arrows(B):
    # Adjust the direction of the arrows based on the zones and applied magnetic field
    for zone in zones:
        u[zone["rows"], zone["cols"]] = np.cos(zone["angle"] + B)
        v[zone["rows"], zone["cols"]] = np.sin(zone["angle"] + B)

    fig, ax = plt.subplots(figsize=(8, 8))

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
    ax.set_title('Ferromagnetism Simulation with B = {:.2f}'.format(B))

    plt.show()

# Use ipywidgets to add a slider for the applied magnetic field
interact(plot_arrows, B=(0, 2*np.pi, 0.1));
