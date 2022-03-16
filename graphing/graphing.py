import matplotlib.pyplot as plt
import math
import numpy as np
from numpy.core.fromnumeric import shape


plt.style.use("bmh")


x_coordinates = np.arange(-10, 10, 0.1)
# y_coordinates = np.sin(x_coordinates)
y_coordinates = x_coordinates ** 3
plt.plot(x_coordinates, y_coordinates, c="green", marker="o")

plt.xlim(-50, 50)
plt.show()



x_coordinates = np.linspace(0, 100, 100)
y_coordinates = np.random.randint(0, 100, size=x_coordinates.shape)
plt.scatter(x_coordinates, y_coordinates)
plt.show()
