import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow

# Define the size of the grid
n = 40

# Initialize the grid
x, y = np.meshgrid(np.arange(n), np.arange(n))

# Initialize the directions of the arrows to simulate ferromagnetism
u = np.ones((n, n))
v = np.zeros((n, n))

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
    u[zone["rows"], zone["cols"]] = np.cos(zone["angle"])
    v[zone["rows"], zone["cols"]] = np.sin(zone["angle"])

# Define the applied magnetic field (x and y components)
Bx = 0.5  # Magnitude of the field in the x-direction
By = 0.5  # Magnitude of the field in the y-direction

# Update the arrow directions based on the applied field
u = u + Bx
v = v + By

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
ax.set_title('Ferromagnetism Simulation with Applied Magnetic Field')

plt.show()
