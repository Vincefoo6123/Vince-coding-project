"""
File: BeeperRowAdv.py
Name:Vince
------------------------------
This program guides Karel to place beepers
along Street 1, even if some beepers are
already present.

The goal is to make sure every corner on
Street 1 has exactly one beeper. The
solution should work for different world
sizes, not just one specific world.
"""

from karel.stanfordkarel import *


def main():
    """
    karel will fill the first street with beeper
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()













####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)