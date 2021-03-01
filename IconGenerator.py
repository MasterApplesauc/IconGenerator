from PIL import Image
icon_sizes = [(16, 16), (32, 32), (48, 48),(64, 64),(128, 128), (255, 255)]
img = Image.open(r'logo.png')
img.save('icon.ico', sizes=icon_sizes)
