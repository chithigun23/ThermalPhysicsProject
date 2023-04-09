import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_ax = 10  # Set x-axis length
num_part_red = 20  # Set number of red particles
num_part_blue = 20  # Set number of blue particles
speed_red = 0.9  # Set speed for red particles
speed_blue = 0.000001  # Set speed for blue particles

fig, ax = plt.subplots()
points_red, = ax.plot([], [], 'o', c='red')  # Set color to red for first set of points
points_blue, = ax.plot([], [], 'o', c='blue')  # Set color to blue for second set of points
ax.set_xlim(0, x_ax)  # Set x-axis limits
ax.set_ylim(0, 1)  # Set y-axis limits

def update(data):
    x_data_red = data[0] + speed_red  # Update x data for red points with speed
    x_data_blue = data[1] + speed_blue  # Update x data for blue points with speed
    points_red.set_data(x_data_red, np.random.rand(num_part_red))  # Update x and y data for red points
    points_blue.set_data(x_data_blue, np.random.rand(num_part_blue))  # Update x and y data for blue points
    return points_red, points_blue,  # Return both sets of points

def generate_points():
    while True:
        x_data = np.linspace(0, x_ax, num_part_red), np.linspace(0, x_ax, num_part_blue)  # Generate evenly spaced x data for red and blue points
        yield x_data  # Yield x data for both sets of points

ani = animation.FuncAnimation(fig, update, generate_points, blit=False, interval=200, cache_frame_data=False)
ani.save('animation.gif', writer='imagemagick', fps=15, save_count=num_part_red + num_part_blue)

plt.show()
