import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

##########################################################
#Define a number N dipoles and n poles aligned with field
N = 6
n = 2
##########################################################

m = np.arange(N) # Create an array of integers from 0 to N-1

# Generate a random sample of 'n' integers between 0 and N-1
down_arrows = np.random.choice(m, N-n, replace=False)

# Plot the line
fig, ax = plt.subplots()

# Plot the arrows
for i in m:
    if i in down_arrows: # If the arrow should face down
        arrow = patches.Arrow(i+1, 0, 0, -1, width=N*0.05, color='black')
    else: # If the arrow should face up
        arrow = patches.Arrow(i+1, 0, 0, 1, width=N*0.05, color='black')
    ax.add_patch(arrow)

# Set the axis limits
plt.xlim(0,N+1)
plt.ylim(-2, 2)

# Add axis labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vertical Line from x=0.5')

# Display the plot
plt.show()
