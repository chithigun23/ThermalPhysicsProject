import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Define Inputs
        self.input_vars = {
            'num_part_red': tk.StringVar(value='20'),
            'num_part_blue': tk.StringVar(value='20'),
            'speed_red': tk.StringVar(value='0.9'),
            'speed_blue': tk.StringVar(value='0.000001')
        }

        # Create input fields
        for i, (key, var) in enumerate(self.input_vars.items()):
            tk.Label(self, text=key).grid(row=i, column=0)
            tk.Entry(self, textvariable=var).grid(row=i, column=1)

        # Create Calculate button
        self.calculate_button = tk.Button(self, text='Calculate', command=self.calculate)
        self.calculate_button.grid(row=len(self.input_vars), column=1)

        # Create Pause/Play button
        self.pause_button = tk.Button(self, text='Pause/Play', command=self.pause_play)
        self.pause_button.grid(row=len(self.input_vars)+1, column=1)

        # Create Save button
        self.save_button = tk.Button(self, text='Save Animation', command=self.save)
        self.save_button.grid(row=len(self.input_vars)+2, column=1)

        # Create matplotlib Figure and Axes
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks([])  # Hide x-axis ticks initially
        self.ax.set_yticks([])  # Hide y-axis ticks initially

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=6)

        # Initialize animation variables
        self.anim = None
        self.anim_running = False
        self.points_red = None
        self.points_blue = None

    def calculate(self):
        # Clear previous plot
        self.ax.cla()

        # Get input values
        self.num_part_red = int(self.input_vars['num_part_red'].get())
        self.num_part_blue = int(self.input_vars['num_part_blue'].get())
        self.speed_red = float(self.input_vars['speed_red'].get())
        self.speed_blue = float(self.input_vars['speed_blue'].get())

        # Plot
        self.ax.set_xlim(0, 10)  # Set x-axis limits
        self.ax.set_ylim(0, 1)  # Set y-axis limits

        self.points_red, = self.ax.plot([], [], 'o', c='red')
        self.points_blue, = self.ax.plot([], [], 'o', c='blue')

        # Hide the ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        # Start animation
        self.anim = FuncAnimation(self.fig, self.update, interval=500, save_count=100)
        self.anim_running = True

        # Draw the plot
        self.canvas.draw()

    def pause_play(self):
        if self.points_red is None or self.points_blue is None:
            return

        if self.anim_running:
            self.anim.event_source.stop()
        else:
            self.anim.event_source.start()
        self.anim_running = not self.anim_running

    def update(self, frame):
        x_data_red = np.random.rand(self.num_part_red)*10  # Randomize x data for red points
        x_data_blue = np.random.rand(self.num_part_blue)*10  # Randomize x data for blue points

        # Update points
        self.points_red.set_data(x_data_red, np.random.rand(self.num_part_red))
        self.points_blue.set_data(x_data_blue, np.random.rand(self.num_part_blue))

        return self.points_red, self.points_blue

    def save(self):
        if self.points_red is None or self.points_blue is None:
            return

        # Generate a unique filename based on input values
        filename = f'animation_{self.num_part_red}_{self.num_part_blue}_{self.speed_red}_{self.speed_blue}.gif'

        # Save the animation as a gif (requires ImageMagick or Pillow)
        self.anim.save(filename, writer='pillow', fps=2)

        print(f'Animation saved as {filename}')

# Create a root window
root = tk.Tk()
app = Application(master=root)

# Start the application
app.mainloop()
