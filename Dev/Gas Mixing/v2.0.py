import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import os
import sys
import subprocess

class Application(tk.Frame):
    R = 8.314  # Gas constant in J/(mol*K)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Define Inputs
        self.input_vars = {
            'Red Particle Number': tk.StringVar(value='5'),
            'Blue Particle Number': tk.StringVar(value='5'),
            'Red Temperature': tk.StringVar(value='300'),  # in K
            'Blue Temperature': tk.StringVar(value='300'),  # in K
            'Red Pressure': tk.StringVar(value='101325'),  # in Pa
            'Blue Pressure': tk.StringVar(value='101325'),  # in Pa
            'Red Volume': tk.StringVar(value='1'),  # in m^3
            'Blue Volume': tk.StringVar(value='1'),  # in m^3
            'FPS': tk.StringVar(value='10'),
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

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
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
        self.num_part_red = int(self.input_vars['Red Particle Number'].get())
        self.temp_red = float(self.input_vars['Red Temperature'].get())
        self.pres_red = float(self.input_vars['Red Pressure'].get())
        self.vol_red = float(self.input_vars['Red Volume'].get())
        
        self.num_part_blue = int(self.input_vars['Blue Particle Number'].get())
        self.temp_blue = float(self.input_vars['Blue Temperature'].get())
        self.pres_blue = float(self.input_vars['Blue Pressure'].get())
        self.vol_blue = float(self.input_vars['Blue Volume'].get())

        fps = float(self.input_vars['FPS'].get())

        # Plot
        self.ax.set_xlim(0, 10)  # Set x-axis limits
        self.ax.set_ylim(0, 1)  # Set y-axis limits

        self.points_red, = self.ax.plot([], [], 'o', c='red')
        self.points_blue, = self.ax.plot([], [], 'o', c='blue')

        # Hide the ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        # Set graph title
        title = f"Red = {self.num_part_red}, Blue = {self.num_part_blue}"
        self.ax.set_title(title)

        # Calculate interval based on FPS
        interval = int(1000 / fps)  # Convert FPS to interval in milliseconds

        # Start animation (paused initially)
        self.anim = FuncAnimation(self.fig, self.update, interval=interval, save_count=100)
        self.pause_play()  # Start in paused state

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
        if self.anim_running:
            # Calculate speed based on temperature (proportional to sqrt(T))
            speed_red = np.sqrt(self.temp_red)
            speed_blue = np.sqrt(self.temp_blue)
            
            # Calculate displacement based on speed and pressure (inversely proportional to P)
            disp_red = speed_red / self.pres_red
            disp_blue = speed_blue / self.pres_blue

            x_data_red = np.random.rand(self.num_part_red) * 10 * disp_red  # Randomize x data for red points
            x_data_blue = np.random.rand(self.num_part_blue) * 10 * disp_blue  # Randomize x data for blue points

            # Update points
            self.points_red.set_data(x_data_red, np.random.rand(self.num_part_red))
            self.points_blue.set_data(x_data_blue, np.random.rand(self.num_part_blue))

        return self.points_red, self.points_blue

    def save(self):
        if self.points_red is None or self.points_blue is None:
            return

        # Get values for file names
        fps = float(self.input_vars['FPS'].get())
        fps_rnd = round(fps)

        # Generate a unique filename based on input values
        filename = f'r{self.num_part_red}_b{self.num_part_blue}_fps{fps_rnd}.gif'

        # Save the animation as a gif
        self.anim.save(filename, writer='pillow', fps=fps)

        print(f'Animation saved as {filename}')

# Create a root window
root = tk.Tk()
app = Application(master=root)

def back_to_menu():
    # This will destroy the current window
    root.destroy()
    # This will run the menu script
    menu_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'MENU', 'menu.py')
    subprocess.Popen([sys.executable, menu_script_path])

# Create a Back button
back_button = tk.Button(root, text="Back", command=back_to_menu)
back_button.pack()

# Start the application
app.mainloop()
