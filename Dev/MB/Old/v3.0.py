import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class Particle:
    """Define physics of elastic collision."""

    def __init__(self, mass, radius, position, velocity):
        """Initialize a Particle object

        mass the mass of particle
        radius the radius of particle
        position the position vector of particle
        velocity the velocity vector of particle
        """
        self.mass = mass
        self.radius = radius

        # last position and velocity
        self.position = np.array(position)
        self.velocity = np.array(velocity)

        # all position and velocities recorded during the simulation
        self.solpos = [np.copy(self.position)]
        self.solvel = [np.copy(self.velocity)]
        self.solvel_mag = [np.linalg.norm(np.copy(self.velocity))]

    def compute_step(self, step):
        """Compute position of next step."""
        self.position += step * self.velocity
        self.solpos.append(np.copy(self.position))
        self.solvel.append(np.copy(self.velocity))
        self.solvel_mag.append(np.linalg.norm(np.copy(self.velocity)))


    def check_coll(self, particle):
        """Check if there is a collision with another particle."""

        r1, r2 = self.radius, particle.radius
        x1, x2 = self.position, particle.position
        di = x2-x1
        norm = np.linalg.norm(di)
        if norm-(r1+r2)*1.1 < 0:
            return True
        else:
            return False


    def compute_coll(self, particle, step):
        """Compute velocity after collision with another particle."""
        m1, m2 = self.mass, particle.mass
        r1, r2 = self.radius, particle.radius
        v1, v2 = self.velocity, particle.velocity
        x1, x2 = self.position, particle.position
        di = x2-x1
        norm = np.linalg.norm(di)
        if norm-(r1+r2)*1.1 < step*abs(np.dot(v1-v2, di))/norm:
            self.velocity = v1 - 2. * m2/(m1+m2) * np.dot(v1-v2, di) / (np.linalg.norm(di)**2.) * di
            particle.velocity = v2 - 2. * m1/(m2+m1) * np.dot(v2-v1, (-di)) / (np.linalg.norm(di)**2.) * (-di)


    def compute_refl(self, step, size):
        """Compute velocity after hitting an edge.
        step the computation step
        size the medium size
        """
        r, v, x = self.radius, self.velocity, self.position
        projx = step*abs(np.dot(v,np.array([1.,0.])))
        projy = step*abs(np.dot(v,np.array([0.,1.])))
        if abs(x[0])-r < projx or abs(size-x[0])-r < projx:
            self.velocity[0] *= -1
        if abs(x[1])-r < projy or abs(size-x[1])-r < projy:
            self.velocity[1] *= -1.

    def get_velocity_vector(self):
        """Get velocity vector for animation"""
        return self.velocity / np.linalg.norm(self.velocity) * np.sqrt(self.solvel_mag[-1])


def solve_step(particle_list, step, size):
    """Solve a step for every particle."""

 # Detect edge-hitting and collision of every particle
    for i in range(len(particle_list)):
        particle_list[i].compute_refl(step,size)
        
        for j in range(i+1, len(particle_list)):
            if particle_list[i].check_coll(particle_list[j]):
                particle_list[i].compute_coll(particle_list[j],step)