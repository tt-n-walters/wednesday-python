import csv
import numpy as np


with open("us-presidents.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)


# print("Read/ len(rows[0]), "columns.")
rows.pop(0)

colours = set()
for row in rows:
    _, _, eye, hair, _ = row
    colours.add(eye)
    colours.add(hair)

colours = list(colours)
# print("Found", len(colours), "unique colours.")
# print(colours)

names = np.array(rows)[:, 0]

converted_rows = []
for i in range(len(rows)):
    name, height, eye, hair, age = rows[i]
    converted = []

    years = int(age[:2])
    days = int(age[9:-4])
    total = years * 365 + days

    converted.append(int(height))
    converted.append(colours.index(eye))
    converted.append(colours.index(hair))
    converted.append(total)
    
    converted_rows.append(converted)

def years(days):
    return round(days / 365, 1)

def days(years):
    return years * 365


data = np.array(converted_rows, dtype="uint16")

# ages = data[:, 3]
# youngest = years(ages.min())
# oldest = years(ages.max())
# average = years(ages.mean())
# print("Youngest:", youngest)
# print("Oldest:", oldest)
# print("Average:", average)


# brown = data == colours.index("brown")

# older = ages > 19000
# print(names[older])


# print("\n\n\n\n")
# youngest = ages.min()
# print(youngest)

# print(names[ages == youngest])



# Oldest president with blue eyes and brown hair

print("colours\n", colours, end="\n\n\n")
print("names\n", names, end="\n\n\n")
print("data\n", data, end="\n\n\n")

blue = colours.index("blue")
brown = colours.index("brown")
blue_eyes = data[:, 1] == blue
brown_hair = data[:, 2] == brown
eye_hair_colours = blue_eyes & brown_hair
filtered = data[eye_hair_colours, 3]
oldest = data[:, 3] == filtered.max()

print(names[oldest])


import matplotlib.pyplot as plt
plt.style.use("ggplot")

heights = data[:, 0]
line = np.linspace(177, 181, 42)
plt.ylim((150, 200))

plt.plot(heights)
plt.plot(line)
plt.show()