# ----------------------------------------------
# -- Practical => Image Mainpulation With Pillow
# ----------------------------------------------
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

from PIL import Image


# Open The Image
myimage = Image.open(r"C:\Users\eyad0\OneDrive\Documents\Screenshot 2024-07-27 170652.png")

# Show The Image

myimage.show()


# My Cropped Image

mybox = (300, 300, 800, 800)    # (left, upper, right, lower)

mynewimage = myimage.crop(mybox)

# Show The New Image

mynewimage.show()

# My Converted Mode Image

myconverted = myimage.convert("L")

myconverted.show()