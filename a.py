import numpy as np
from numba import njit, jit

@njit
def gen_points(radius):
    return np.array([([1,2,3]), ([4,5,6])])

@njit
def iterate_points(points):
    for i in range(points.shape[0]):
        points[i] = points[i] + 1

points = gen_points(2)
print(points.shape)
# iterate_points(points)