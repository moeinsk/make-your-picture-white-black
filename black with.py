from PIL import Image
img = Image.open("python-powered-w-140x56.png")
img.convert('L').save('new pik.png')