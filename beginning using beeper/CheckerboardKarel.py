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
    """
    Makes Karel turn 90 degrees to the right by executing three left turns
    """
    for i in range(3):
        turn_left()


def move_odd_line():
    """
    Fills an odd-numbered row with beepers in a staggered pattern.
    Starts by placing a beeper at the first available spot and continues
    moving two steps at a time to maintain the gap.
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
    Fills an even-numbered row with beepers.
    The logic accounts for the final state of the previous row to ensure 
    the checkerboard pattern remains consistent across the entire world.
    """
    if on_beeper():
        # If the previous row ended with a beeper, start this row by moving first
        while front_is_clear():
            if front_is_clear():
                move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        # If the previous row ended without a beeper, start this row with a beeper
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
    Main execution loop that alternates between odd and even row filling strategies.
    Uses a 'state reminder' to bridge the logic between horizontal rows.
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
