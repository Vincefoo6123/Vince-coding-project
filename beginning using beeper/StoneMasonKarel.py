"""
File: StoneMasonKarel.py
Name: Vince
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_and_check():
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()
    turn_right()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()
    turn_left()

def main():
    while front_is_clear():
        turn_and_check()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
