import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random points within a unit cube
np.random.seed() #Creates random number without seed, differing random numbers when executed.
num_points = 50 #Number of particles in simulation
points = np.random.rand(num_points, 3)  # Random points in [0, 1) interval

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') #first and only 3d subplot, for this version

# Plot the random points, x y and z values. And gives colour. 
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o', label='Random Points')

# Set axes limits of the plot
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

# Add labels and title for plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Random Points in a Unit Cube')

# Show the plot
plt.show()
