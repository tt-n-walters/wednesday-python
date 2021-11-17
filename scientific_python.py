import random
from time import perf_counter

import numpy as np

print(perf_counter(), "Generating numbers...")

# Slowest possible version
# numbers = []
# for _ in range(50_000_000):
#     n = np.random.random()
#     numbers.append(n)


# Numpy version 1
# print("Numpy version 1")
# numbers = np.zeros(shape=(5_000_000))
# for i in range(5_000_000):
#     n = np.random.random()
#     numbers[i] = n
# print(numbers.shape)
# print(numbers.dtype)

# Best Numpy version

# print("Best Numpy version")
numbers = np.random.random(500_000_000)
print(perf_counter(), "Finished generating.")
print(perf_counter(), "Calculating average.")
average = numbers.mean()
print(average)
print(perf_counter(), "Finished calculating.")

# Pure Python version

numbers = []
for i in range(50_000_000):
    n = random.random()
    numbers.append(n)


print(perf_counter(), "Finished generating.")
print(perf_counter(), "Calculating average.")

total = sum(numbers)
average = total / len(numbers)
print(average)

print(perf_counter(), "Finished calculating.")
