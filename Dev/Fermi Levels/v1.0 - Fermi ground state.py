import matplotlib.pyplot as plt
import numpy as np

def plot_large_dots(n,d):
    fig, ax = plt.subplots()
    
    # Generate the y-coordinates for the large dots
    y_coords = np.arange(0, n*d,d)
    
    # Plot the large dots as scatter points
    ax.scatter(np.zeros_like(y_coords), y_coords, s=100, color='black')
    
    # Hide the x-axis ticks and show relavant yaxis ticks
    ax.set_xticks([])
    ax.set_yticks(np.arange(0,n*d,d))
    
    # Set the y-axis limits
    ax.set_ylim(-1, n*d + 1)
    
    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Ground-state Fermi energy')
    
    # Calculate the energy sum
    energy_sum = np.sum(y_coords)
    
    # Add text onto the plot
    ax.text(0.04, n*d-(d/2), 'E=' + str(energy_sum), fontsize=12, color='red',  bbox=dict(facecolor='black', alpha=0.15))

    # Show plot
    plt.show()
    

# Usage example
num_large_dots = 5
diff = 4
plot_large_dots(num_large_dots,diff)
