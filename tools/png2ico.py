from PIL import Image

logo = Image.open("./src/icon.png")

logo.save("./src/icon.ico", format='ICO')
