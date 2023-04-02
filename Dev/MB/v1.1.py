import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

k = 1.38e-23
m = 6.63e-26
T = 298.15 # temperature in Kelvin
v = np.random.normal(0, np.sqrt(k*T/m), 1000) #Boltzmann's Equation for particle velocity

fig, ax = plt.subplots()
hist, bins = np.histogram(v, bins=50, density=True, range=[0, 1000])
x = (bins[:-1] + bins[1:]) / 2
line, = ax.plot(x, (m/(2*np.pi*k*T))**1.5 * 4*np.pi*x**2 * np.exp(-m*x**2/(2*k*T)), 'r')
ax.hist(v, bins=bins, alpha=0.5, range=[0, 1000])

def update(t):
    T = t + 273.15
    hist[:] = np.histogram(v, bins=50, density=True, range=[0, 1000])[0]
    line.set_ydata((m/(2*np.pi*k*T))**1.5 * 4*np.pi*line.get_xdata()**2 * np.exp(-m*line.get_xdata()**2/(2*k*T)))

slider = widgets.FloatSlider(min=-50, max=50, step=0.1, value=0)
widgets.interact(update, t=slider)

plt.show()
