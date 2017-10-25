from PIL import Image
import re

image = Image.open("cave.jpg")
one = Image.new("RGB", [320,240])
two = Image.new("RGB", [320,240])
row = 0
col = 0

for col in range(0, image.size[0]):
	print col
	for row in range(0, image.size[1]):
		print row
		if(row%2 == 0):
			one.putpixel((col/2, row/2), image.getpixel((col, row)))
		else:
			two.putpixel((col/2, row/2), image.getpixel((col, row)))
one.save("test1", "JPEG")
two.save("test2", "JPEG")