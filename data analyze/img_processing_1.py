"""
This program implements some basic
functionality similar to a simple Photoshop program.

It works with SimpleImage objects and their pixels.
Each image is made up of many pixels, and each pixel has
position and color properties such as x, y, red, green, and blue,
as well as image width and height information.
"""

from simpleimage import SimpleImage


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    filepath = "images/stanford.jpg"
    img = SimpleImage(filepath)
    img.show()
    red_channel(img)
    pass


def red_channel(img):
    """
    remove all blue and green colors from the photo to enhance
    the red channel of its pixels (the R in RGB).
    ---------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the updated image with all pixels turning red
    """
    for pixel in img:
        pixel.green = 0
        pixel.blue = 0
    img.show()
    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
