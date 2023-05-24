import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Define a function that computes the Maxwell-Boltzmann distribution for a given velocity, temperature, and mass
def maxwell_boltzmann(v, T, m):
    k = 1.380649e-23  # Boltzmann constant (J/K)
    return (m / (2 * np.pi * k * T)) ** 1.5 * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k * T))

# Set the temperature, mass, and number of particles
T = 300
m = 4.65e-26
num_particles = 500
k = 1.380649e-23

# Generate random initial positions and velocities for particles
particles = np.random.uniform(-50, 50, (num_particles, 3))
velocities = np.random.normal(0, np.sqrt(k * T / m), (num_particles, 3))

# Create a figure with a 3D plot of the particles
fig = plt.figure(figsize=(12, 7))
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_xlim(-50, 50)
ax1.set_ylim(-50, 50)
ax1.set_zlim(-50, 50)
ax1.set_title('Particles in Motion')
particles_plot = ax1.scatter(*particles.T, s=4)

# Show the plot
plt.show()
