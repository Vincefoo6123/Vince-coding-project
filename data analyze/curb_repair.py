"""
File: curb_repair.py
Name:
-------------------------------
This program demonstrates how to
detect red pixels in a curb image
and convert them to grayscale.

By changing the curb area from red
to gray, the program simulates
turning the curb into an available
parking space.
"""


from simpleimage import SimpleImage

THRESHOLD = 1.12


def main():
    img = SimpleImage("images/curb.png")
    for pixel in img:
        avg = (pixel.red + pixel.blue + pixel.green)//3
        if pixel.red > THRESHOLD*avg:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':

    main()
