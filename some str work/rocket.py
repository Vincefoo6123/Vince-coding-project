"""
File: rocket.py
Name:Vince
-----------------------
This program implements a console-based application that
draws an ASCII art rocket.

The size of the rocket is determined by a constant named
SIZE, which is defined at the top of the file. The output
format should match the sample run shown in the Assignment 3 handout.
"""

# This constant determines rocket size.
SIZE = 2


def head():
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(" ", end="")
        for j in range(1 + i):
            print("/", end="")
        for j in range(1 + i):
            print("\\", end="")
        print("")


def belt():
    print("+", end="")
    for i in range(2 * SIZE):
        print("=", end="")
    print("+")


def upper():
    for i in range(SIZE):
        print("|", end="")
        for j in range((SIZE - 1) - i):
            print(".", end="")
        for j in range(1 + i):
            print("/", end="")
            print("\\", end="")
        for j in range((SIZE - 1) - i):
            print(".", end="")
        print("|", end="")
        print("")


def lower():
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE - i):
            print("\\", end="")
            print("/", end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print(" ")


def main():
    """
    TODO:
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()
    pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
