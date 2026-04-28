"""
File: PotholeFilling.py
Name: Vince
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def go_in():
    move()
    turn_right()
    move()
def go_out():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()
def put_99():
    for i in range(99):
        put_beeper()
    pass


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
