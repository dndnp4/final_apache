from os import remove
from PIL import Image

img = Image.open('1.jpg')
image = img.resize((350,420))
image.save('image1.jpg')

target_image = Image.open('id_card.jpg')
add_image = Image.open('image1.jpg')
target_image.paste(im = add_image,box=(75,245))
target_image.save('onepick.jpg')

remove('image1.jpg')


