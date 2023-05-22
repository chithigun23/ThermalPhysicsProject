import numpy as np
import matplotlib.pyplot as plt

# Define the number of total dipoles in the paramagnet (N) and the number of dipoles aligned with the field (n)
N = 4
n = 4
a = (-(2)*n) + N

# Define the angle range for the semicircle
theta = np.linspace(0, np.pi, 100)

# Calculate the x and y coordinates of the points on the semicircle
x = N * np.cos(theta)
y = N * np.sin(theta)

# Calculate the x and y coordinates for the point representing 'n' on the semicircle
x_a = a
y_a = np.sqrt(N**2 - (x_a)**2)

# Plot the semicircle
plt.plot(x, y, 'b', linewidth=2)
plt.plot(x_a, y_a, 'ro')  # Plot red dot at the respective 'n' value on the semicircle
plt.axhline(0, color='black', linewidth=0.5)  # Draw the y-axis
plt.axvline(0, color='black', linewidth=0.5)  # Draw the x-axis
plt.axis('equal')  # Set equal scaling on the x and y axes

# Set ticks on the x-axis
x_intercepts = [-N, N, 0]
plt.xticks(x_intercepts)

plt.yticks([])  # Remove y-axis ticks

plt.ylim(0, N + 0.1)  # Set y-axis limit
plt.xlabel('Internal Energy ($U/μB$)', fontsize=12)  # Replace (mu) with the Greek letter μ
plt.ylabel('Entropy ($S/k$)', fontsize=12)  # Replace (mu) with the Greek letter μ
plt.title('Temperature Plot', fontsize=14)

# Display the plot
plt.show()
