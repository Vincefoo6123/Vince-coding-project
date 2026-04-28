"""
File: CheckerboardKarel.py
Name: Vince
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()


def move_odd_line():
    """

    """
    put_beeper()
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()


def move_even_line():
    """

    """
    if on_beeper():
        while front_is_clear():
            if front_is_clear():
                move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        move()
        put_beeper()
        while front_is_clear():
            if front_is_clear():
                move()
            if front_is_clear():
                move()
                put_beeper()


def main():
    """
    write odd and even number

    """
    while True:
        move_odd_line()
        turn_left()
        remind_beeper = on_beeper()
        if not front_is_clear():
            break
        move()
        turn_left()
        if not remind_beeper:
            put_beeper()
        move_even_line()
        turn_right()
        if not front_is_clear():
            break
        move()
        turn_right()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
