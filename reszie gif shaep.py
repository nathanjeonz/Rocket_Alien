from PIL import Image

img = Image.open("rkt.gif")
# Resize the image to 100x100 pixels
img = img.resize((50, 100))
# Save the resized image
img.save("rkt_resized.gif")