import matplotlib.pyplot as plt
import numpy as np

#Define a number n
n=4
m = np.arange(n+1)  # Create an array of integers from 0 to n
print(m)

x = [m,m]
y = [0, 1]

# Plot the line
plt.plot(x, y)

# Set the axis limits
plt.xlim(0,n+1)
plt.ylim(0, 2)

# Add axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vertical Line from x=0.5')

# Display the plot
plt.show()
