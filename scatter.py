# Scatter Plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 3, 5, 6, 2, 8, 14])
y = np.array([20, 30, 50, 60, 25, 80, 140])
plt.scatter(x, y)

# Plot 2:
# Day 2 the age and speed of the cars 10 cars
x = np.array([0, 3, 5, 6, 2, 8, 14, 19, 20, 13])
y = np.array([80, 85, 90, 100, 125, 180, 40, 30, 47, 90])
plt.scatter(x, y, color="Pink")

plt.show()
