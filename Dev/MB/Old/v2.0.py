import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ipywidgets as widgets
from IPython.display import display

k = 1.38e-23       # Boltzmann constant
m = 4.65e-26       # Mass of gas particles
T = 300            # Temperature of gas
n = 1000           # Number of gas particles

v = np.sqrt((k*T)/m)*np.random.randn(n)

fig, ax = plt.subplots()
hist, bins, _ = ax.hist(v, bins=50, density=True, alpha=0.5, range=[0, 1000])
x = np.linspace(0, 1000, 1000)
line, = ax.plot(x, (m/(2*np.pi*k*T))**1.5 * 4*np.pi*x**2 * np.exp(-m*x**2/(2*k*T)), 'r')


def update_hist(t):
    global v
    v += 0.1*np.random.randn(n)
    hist[0], hist[1], _ = ax.hist(v, bins=50, density=True, alpha=0.5, range=[0, 1000])
    line.set_ydata((m/(2*np.pi*k*T))**1.5 * 4*np.pi*line.get_xdata()**2 * np.exp(-m*line.get_xdata()**2/(2*k*T*t)))
    ax.set_ylim(0, 0.003)
    ax.set_xlim(0, 1000)
    ax.set_xlabel('Velocity (m/s)')
    ax.set_ylabel('Probability density')
    ax.set_title('Maxwell-Boltzmann Distribution t={}'.format(t))

t_slider = widgets.FloatSlider(
    value=1.0,
    min=0.1,
    max=10.0,
    step=0.1,
    description='Time:',
    readout_format='.1f',
    layout={'width': '500px'}
)

def on_value_change(change):
    update_hist(change.new)

t_slider.observe(on_value_change, names='value')

display(t_slider)
display(fig)

update_hist(t_slider.value)

plt.show()
