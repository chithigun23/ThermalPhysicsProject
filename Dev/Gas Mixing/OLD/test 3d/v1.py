import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def maxwell_boltzmann(v, T, m):
    k = 1.380649e-23  # Boltzmann constant (J/K)
    return (m / (2 * np.pi * k * T)) ** 1.5 * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k * T))

def update(val):
    T = temperature_slider.val
    m = mass_slider.val
    num_particles = int(num_particles_slider.val)

    # Generate random initial positions and velocities for particles
    particles = np.random.uniform(-50, 50, (num_particles, 3))
    velocities = np.random.normal(0, np.sqrt(k * T / m), (num_particles, 3))

    particles_plot._offsets3d = particles.T
    v = np.linspace(0, 1500, 100)
    hist.set_data(v, num_particles * maxwell_boltzmann(v, T, m))

    fig.canvas.draw_idle()

# Parameters
T = 300
m = 4.65e-26
num_particles = 500
k = 1.380649e-23

# Generate random initial positions and velocities for particles
particles = np.random.uniform(-50, 50, (num_particles, 3))
velocities = np.random.normal(0, np.sqrt(k * T / m), (num_particles, 3))

fig = plt.figure(figsize=(12, 7))

# 3D plot of particles
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlim(-50, 50)
ax1.set_ylim(-50, 50)
ax1.set_zlim(-50, 50)
ax1.set_title('Particles in Motion')
particles_plot = ax1.scatter(*particles.T, s=5)

# Temperature distribution plot
ax2 = fig.add_subplot(122)
ax2.set_xlim(0, 1500)
ax2.set_ylim(0, 0.0025)
ax2.set_title('Temperature Distribution')
ax2.set_xlabel('Velocity (m/s)')
ax2.set_ylabel('Probability Density')
v = np.linspace(0, 1500, 100)
hist, = ax2.plot(v, num_particles * maxwell_boltzmann(v, T, m), lw=2)

# Sliders
slider_ax1 = plt.axes([0.2, 0.15, 0.5, 0.03])
slider_ax2 = plt.axes([0.2, 0.1, 0.5, 0.03])
slider_ax3 = plt.axes([0.2, 0.05, 0.5, 0.03])

temperature_slider = Slider(slider_ax1, 'Temperature (K)', 10, 1000, valinit=T, valstep=10)
mass_slider = Slider(slider_ax2, 'Mass (kg)', 1e-26, 1e-25, valinit=m, valstep=1e-27)
num_particles_slider = Slider(slider_ax3, 'Num Particles', 10, 2000, valinit=num_particles, valstep=10)

temperature_slider.on_changed(update)
mass_slider.on_changed(update)
num_particles_slider.on_changed(update)

plt.show()

