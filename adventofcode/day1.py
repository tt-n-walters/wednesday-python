from aoc_tools import get_input
import numpy as np


inputs = get_input(1)
depths = np.array([int(n) for n in inputs.splitlines()])


triples = depths[ : -2] + depths[1 : -1] + depths[2 : ]

changes = triples[1 : ] - triples[ : -1]
increases = changes > 0
answer = increases.sum()

print(answer)