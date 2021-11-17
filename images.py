from PIL import Image
from time import perf_counter

print(perf_counter(), "Reading image...")

filename = "images/100.jpg"
image = Image.open(filename)

print(perf_counter(), "Resolution:", image.width, image.height)
total_pixels = image.width * image.height
print(perf_counter(), "Total pixels:", total_pixels)

print(perf_counter(), "Extracting pixels...")
pixels = list(image.getdata())

print(perf_counter(), "Processing image...")
new_pixels = []
for pixel in pixels:
    r, g, b = pixel
    average = sum(pixel) // 3
    new_pixel = (average, average, average)
    new_pixels.append(new_pixel)
    

print(perf_counter(), "Saving new image.")
new_image = Image.new(mode="RGB", size=image.size)
new_image.putdata(new_pixels)
new_image.save("images/100_bw.jpg")
print(perf_counter(), "Saved.")