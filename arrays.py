import numpy as np

x = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
print(type(x))

x_a = np.array(x)
print(type(x_a))
print(x_a.shape)


ns = np.arange(1, 101).reshape(10, 10)
print(ns)
print(ns[7:9, 3:6])
print(ns.shape)


r = np.array([[0, 0, 0], [0, 0, 0]])
ns[5:9:2, 2:8:2] = r

print(ns)
