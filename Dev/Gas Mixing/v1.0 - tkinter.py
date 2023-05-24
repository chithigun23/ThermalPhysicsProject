import numpy as np
import matplotlib.pyplot as plt
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

        # Create matplotlib Figure and Axes
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks([])  # Hide x-axis ticks initially
        self.ax.set_yticks([])  # Hide y-axis ticks initially

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=4)

    def calculate(self):
        # Clear previous plot
        self.ax.cla()

        # Get input values
        num_part_red = int(self.input_vars['num_part_red'].get())
        num_part_blue = int(self.input_vars['num_part_blue'].get())
        speed_red = float(self.input_vars['speed_red'].get())
        speed_blue = float(self.input_vars['speed_blue'].get())

        # Plot
        self.ax.set_xlim(0, 10)  # Set x-axis limits
        self.ax.set_ylim(0, 1)  # Set y-axis limits

        x_data_red = np.linspace(0, 10, num_part_red) + speed_red  # Update x data for red points with speed
        x_data_blue = np.linspace(0, 10, num_part_blue) + speed_blue  # Update x data for blue points with speed

        # Set color to red for first set of points
        self.ax.plot(x_data_red, np.random.rand(num_part_red), 'o', c='red')

        # Set color to blue for second set of points
        self.ax.plot(x_data_blue, np.random.rand(num_part_blue), 'o', c='blue')

        # Hide the ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        # Redraw the canvas (needed for clearing previous plot)
        self.canvas.draw()

# Create a root window
root = tk.Tk()
app = Application(master=root)

# Start the application
app.mainloop()
