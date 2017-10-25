from PIL import Image
import re

image = Image.open("oxygen.png")
row = 44
blocks = []
prevRgb = (0,0,0)
maxPixelsInBlob = 7
pixelCount = 0
for col in range(0, 608):
    rgb = image.getpixel((col, row))
    if rgb != prevRgb or pixelCount == maxPixelsInBlob:
        blocks.append(chr(rgb[0]))
        pixelCount = 0
        prevRgb = rgb
    else:
        pixelCount += 1

pattern = re.compile(r"\d+")
output = "".join(char for char in blocks)
print(output)
ints = (int(i) for i in pattern.findall(output))
print("".join(chr(i) for i in ints))
