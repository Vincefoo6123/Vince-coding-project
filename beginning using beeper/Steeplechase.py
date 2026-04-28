"""
File: Steeplechase.py
Name: Vince
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()
def jump():
    up()
    turn()
    down()
def up():
    """
    pre:east
    post:north
    """
    turn_left()
    while not right_is_clear():
        move()
def turn():
    """
    pre:north
    post:east
    """
    turn_right()
    move()
    turn_right()
def down():
    """
    pre:south
    post:east
    """
    while front_is_clear():
        move()
    turn_left()
def main():
    """
    use for loop to cross 11 walls and approach the final spot
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
