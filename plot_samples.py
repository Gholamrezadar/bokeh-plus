import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# A list of 2D points
def gen_points(radius):
    return np.array([
        radius*2.0* np.array([1.000000, 0.000000]),
        radius*2.0* np.array([0.707107, 0.707107]),
        radius*2.0* np.array([-0.000000, 1.000000]),
        radius*2.0* np.array([-0.707107, 0.707107]),
        radius*2.0* np.array([-1.000000, -0.000000]),
        radius*2.0* np.array([-0.707106, -0.707107]),
        radius*2.0* np.array([0.000000, -1.000000]),
        radius*2.0* np.array([0.707107, -0.707107]),
        radius*4.0* np.array([1.000000, 0.000000]),
        radius*4.0* np.array([0.923880, 0.382683]),
        radius*4.0* np.array([0.707107, 0.707107]),
        radius*4.0* np.array([0.382683, 0.923880]),
        radius*4.0* np.array([-0.000000, 1.000000]),
        radius*4.0* np.array([-0.382684, 0.923879]),
        radius*4.0* np.array([-0.707107, 0.707107]),
        radius*4.0* np.array([-0.923880, 0.382683]),
        radius*4.0* np.array([-1.000000, -0.000000]),
        radius*4.0* np.array([-0.923879, -0.382684]),
        radius*4.0* np.array([-0.707106, -0.707107]),
        radius*4.0* np.array([-0.382683, -0.923880]),
        radius*4.0* np.array([0.000000, -1.000000]),
        radius*4.0* np.array([0.382684, -0.923879]),
        radius*4.0* np.array([0.707107, -0.707107]),
        radius*4.0* np.array([0.923880, -0.382683]),
        radius*6.0* np.array([1.000000, 0.000000]),
        radius*6.0* np.array([0.965926, 0.258819]),
        radius*6.0* np.array([0.866025, 0.500000]),
        radius*6.0* np.array([0.707107, 0.707107]),
        radius*6.0* np.array([0.500000, 0.866026]),
        radius*6.0* np.array([0.258819, 0.965926]),
        radius*6.0* np.array([-0.000000, 1.000000]),
        radius*6.0* np.array([-0.258819, 0.965926]),
        radius*6.0* np.array([-0.500000, 0.866025]),
        radius*6.0* np.array([-0.707107, 0.707107]),
        radius*6.0* np.array([-0.866026, 0.500000]),
        radius*6.0* np.array([-0.965926, 0.258819]),
        radius*6.0* np.array([-1.000000, -0.000000]),
        radius*6.0* np.array([-0.965926, -0.258820]),
        radius*6.0* np.array([-0.866025, -0.500000]),
        radius*6.0* np.array([-0.707106, -0.707107]),
        radius*6.0* np.array([-0.499999, -0.866026]),
        radius*6.0* np.array([-0.258819, -0.965926]),
        radius*6.0* np.array([0.000000, -1.000000]),
        radius*6.0* np.array([0.258819, -0.965926]),
        radius*6.0* np.array([0.500000, -0.866025]),
        radius*6.0* np.array([0.707107, -0.707107]),
        radius*6.0* np.array([0.866026, -0.499999]),
        radius*6.0* np.array([0.965926, -0.258818]),
    ])


# Plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.0, 1.0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, which='both')
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')

# Plot the points
radius = 0.1
points = gen_points(radius)
ax.scatter(points[:,0], points[:,1], s=4, c='r')


plt.show()
