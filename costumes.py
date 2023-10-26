import sys
from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)

images[0].save(
    "comstumes.gif", 
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0
)

#to run call the files you want to animate
