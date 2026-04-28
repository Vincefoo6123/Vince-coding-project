"""
File: CollectNewspaperKarel.py
Name: Vince
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code
to guide Karel to walk to the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()
def go_and_pick_newspaper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
def go_back():
    turn_left()
    turn_left()
    for i in range(3):
        move()
    turn_right()
    move()
    put_beeper()
    turn_right()
def main():
    """
    first on 4 3 and face East
    then go to 3 6 and pick the beeper
    final turn back to 4 3 and face East

    """
    go_and_pick_newspaper()
    go_back()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
