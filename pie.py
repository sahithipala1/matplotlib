import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels)
plt.show()
