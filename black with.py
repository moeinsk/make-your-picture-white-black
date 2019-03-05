#writed by moein
from PIL import Image
img = Image.open("your originally pic")
img.convert('L').save('new pik.png')
#thise is python's power
