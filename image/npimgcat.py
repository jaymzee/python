"""
read an image
convert it to a numpy array (for image processing)
display the image in the terminal (iTerm2 or mintty)
"""

from imgcat import imgcat
import numpy as np
from PIL import Image

im = np.asarray(Image.open('treefrog.png'))
print(type(im), im.shape, im.dtype)
imgcat(im)
