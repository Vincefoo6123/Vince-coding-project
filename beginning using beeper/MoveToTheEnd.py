"""
File: MoveToTheEnd.py
Name:VINCE
------------------------
This program demonstrates how to use a
while loop to move Karel to the end of
a row in the Karel world.

By checking whether the front is clear,
Karel will keep moving forward until it
reaches the end of the row.
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        move()
    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
