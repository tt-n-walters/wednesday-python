import pandas as pd
import random

ns = [random.randint(1, 20) for _ in range(6)]
print(ns)


series = pd.Series(ns)
print(series)
print(series[2:4])
