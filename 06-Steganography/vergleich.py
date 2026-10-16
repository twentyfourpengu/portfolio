"""
Macht sichtbar, welche Pixel sich zwischen original.png und geheim.png unterscheiden.
Schwarz = unverändert, Weiß = verändert.
Benötigt: pip3 install pillow
"""
from PIL import Image, ImageChops

a = Image.open("IMG_1311.png").convert("RGB")
b = Image.open("geheim.png").convert("RGB")
diff = ImageChops.difference(a, b).point(lambda x: 255 if x else 0)
diff.save("unterschied.png")
print("Gespeichert als 'unterschied.png'")
