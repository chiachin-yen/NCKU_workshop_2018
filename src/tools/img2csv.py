import os
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))

im = Image.open(os.path.join(script_dir, 'example.jpg'))  # abs path to file

# load the pixel info
pix = im.load()

# get a tuple of the x and y dimensions of the image
width, height = im.size

# open a file to write the pixel data
with open('example.csv', 'w+') as f:

    # read the details of each pixel and write them to the file
    for y in range(height):
        row = []
        for x in range(width):
            row.append(str(int(pix[x, y][0]*0.2126
                               + pix[x, y][1]*0.7152
                               + pix[x, y][2]*0.0722)))
        f.write(','.join(row)+'\n')
