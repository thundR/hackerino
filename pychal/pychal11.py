from PIL import Image
import re

image = Image.open("cave.jpg")
one = Image.new("RGB", [320,240])
two = Image.new("RGB", [320,240])
row = 0
col = 0

for col in range(0, image.size[0]):
	for row in range(0, image.size[1]):
		if(row%2 == 0):
			one.putpixel((col//2, row//2), image.getpixel((col, row)))
		else:
			two.putpixel((col//2, row//2), image.getpixel((col, row)))
one.save("test1.jpg", "JPEG")
two.save("test2.jpg", "JPEG")