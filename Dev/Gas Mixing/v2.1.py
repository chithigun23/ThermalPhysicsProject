import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 0.0821  # Ideal gas constant
T = 300  # Temperature (K)
V = 1  # Volume (L)

# Parameters
num_particles = 100  # Number of particles
time_steps = 1000  # Number of time steps
dt = 0.01  # Time step size

# Initialize positions and velocities
positions = np.random.rand(num_particles) * V
velocities = np.random.randn(num_particles)

# Initialize pressure
pressure = 0

# Run simulation
for t in range(time_steps):
    # Update positions
    positions += velocities * dt

    # Check for collisions with walls
    collisions = np.where((positions < 0) | (positions > V))[0]
    velocities[collisions] *= -1

    # Update pressure
    pressure += len(collisions) / (V * dt)

# Calculate average pressure
pressure /= time_steps

# Calculate number of moles using Ideal Gas Law
n = pressure * V / (R * T)

print(f"Number of moles: {n}")
