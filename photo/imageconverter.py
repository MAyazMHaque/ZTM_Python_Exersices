import sys
import os
from PIL import Image

# get the image and utpu folder form the user (argument)
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exist if not then create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop throught the folder which converts jpg to png

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All good!')