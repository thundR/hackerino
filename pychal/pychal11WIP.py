from PIL import Image
import math

srcImage = Image.open("cave.jpg")
halfHeight = math.floor(srcImage.width / 2)
halfWidth = math.floor(srcImage.height / 2)
image1 = Image.new(srcImage.mode, (halfWidth, halfHeight))
image2 = Image.new(srcImage.mode, (halfWidth, halfHeight))
#stupid sexy python one liners
data = srcImage.getdata()
data1 = data[1::2]
data2 = data[0::2]

image1.putdata(data1)
image2.putdata(data2)
image1.save("image1.jpg")
image2.save("image2.jpg")