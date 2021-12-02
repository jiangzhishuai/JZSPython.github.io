from scipy import ndimage
import numpy as np

a = np.array([
    [0, 0, 0, 0],
    [0, 1, 0, 0],

    [0, 2, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 2, 0, 1],
    [2, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 0, 0]

])

b = np.mean(a, axis=0)
for a in range(0, 9, 1):
   print(b[a])

