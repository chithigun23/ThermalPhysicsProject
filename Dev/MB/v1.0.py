import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 1.38e-23       # Boltzmann constant
m = 4.65e-26       # Mass of gas particles
T = 300            # Temperature of gas
n = 1000           # Number of gas particles

v = np.sqrt((k*T)/m)*np.random.randn(n)

fig, ax = plt.subplots()
ax.hist(v, bins=50, density=True, alpha=0.5, range=[0, 1000])

x = np.linspace(0, 1000, 1000)
ax.plot(x, (m/(2*np.pi*k*T))**1.5 * 4*np.pi*x**2 * np.exp(-m*x**2/(2*k*T)), 'r')

def update(num):
    global v
    v += 0.1*np.random.randn(n)
    ax.clear()
    ax.hist(v, bins=50, density=True, alpha=0.5, range=[0, 1000])
    ax.plot(x, (m/(2*np.pi*k*T))**1.5 * 4*np.pi*x**2 * np.exp(-m*x**2/(2*k*T)), 'r')
    ax.set_ylim(0, 0.003)
    ax.set_xlim(0, 1000)
    ax.set_xlabel('Velocity (m/s)')
    ax.set_ylabel('Probability density')
    ax.set_title('Maxwell-Boltzmann Distribution t={}'.format(num))

ani = animation.FuncAnimation(fig, update, frames=1000, interval=50, blit=False)
plt.show()
