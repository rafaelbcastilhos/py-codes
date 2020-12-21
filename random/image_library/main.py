import PIL
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

image = Image.open("vancouver.jpg")

image_gray = image.convert(mode="L")

image.thumbnail((100, 100))
image_resize = image.resize((200, 200))


image.save("thumbnail.jpg")
image_resize.save("image_resize.jpg")