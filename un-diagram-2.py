# Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points)
plt.show()
