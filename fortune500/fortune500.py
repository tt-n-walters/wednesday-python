# %%
import requests
import csv
import numpy as np

# %%
url = "https://raw.githubusercontent.com/cmusam/fortune500/master/csv/fortune500-{year}.csv"
years = range(1955, 2020)
urls = [url.format(year=year) for year in years]

# %%
raw_data = {}
for year, url in zip(years, urls):
    print(f"Downloading {year} data...")
    r = requests.get(url)
    raw_data[year] = r.text

# %%
data = {}
for year, raw_string in raw_data.items():
    year_data = list(csv.reader(raw_string.splitlines()))
    year_data.pop(0)

    for row in year_data:
        if row[3] in ("N.A.", ""):
            row[3] = "0"
    
    data[year] = year_data

# %%
from collections import Counter
counted = Counter([row[3] for year in data.values() for row in year])
counted.most_common(5)

# %%
names = np.array([row[1] for year in data.values() for row in year]).reshape((-1, 500))
revenues = np.array([row[2] for year in data.values() for row in year], dtype=float).reshape((-1, 500))
profits = np.array([row[3] for year in data.values() for row in year], dtype=float).reshape((-1, 500))

# %%
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# %%
average_profits = profits.mean(axis=1)
average_revenues = revenues.mean(axis=1)

# %%
plt.plot(years, average_profits, marker=".", label="Profit")
plt.ylabel("$ (millions)")
plt.xlabel("Year")
plt.legend()
plt.show()

# %%

plt.plot(years, average_revenues, marker=".", label="Revenues", c="b")
plt.ylabel("$ (millions)")
plt.xlabel("Year")
plt.legend()
plt.show()


