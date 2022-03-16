from PIL import Image
from time import perf_counter
import numpy as np


print(perf_counter(), "Reading image...")

filename = "images/100.jpg"
image = Image.open(filename)

print(perf_counter(), "Resolution:", image.width, image.height)
total_pixels = image.width * image.height
print(perf_counter(), "Total pixels:", total_pixels)

print(perf_counter(), "Extracting pixels...")
array = np.array(image)

print(perf_counter(), "Processing image...")
# average = array.mean(axis=2).astype("uint8")
# pixels = np.repeat(average, 3).reshape(image.height, image.width, 3)

new_image = array[:, ::-1, :]


print(perf_counter(), "Saving new image.")
new_image = Image.fromarray(new_image)
new_image.save("images/100_new.jpg")
print(perf_counter(), "Saved.")
