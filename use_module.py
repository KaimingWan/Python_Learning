__author__ = 'Kaiming'

from PIL import Image

im = Image.open('D:/banner.jpg')
print(im.format, im.size, im.mode)
# im.thumbnail((200,100))
# im.save('small_banner.jpg','JPEG')
