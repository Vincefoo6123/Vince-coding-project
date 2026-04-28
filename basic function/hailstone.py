"""
File: hailstone.py
Name:Vince
-----------------------
This program implements a console-based simulation of the
Hailstone sequence, as defined by Douglas Hofstadter.

Starting from a user-provided number, the program repeatedly
applies the Hailstone rules and prints each step. The output
format should match the sample run shown in the Assignment 2 handout.
"""


def main():
    """
    test if its odd or even  if odd set number to be 3n+1
    else set number to divisible to 2
    also record how much steps it takes
    """
    print("this program computes Hailstone sequences.")
    number = int(input("Please enter a number:"))
    step = 0
    while not number == 1:
        lest = number % 2
        if lest == 1:
            print(number, end="")
            print(" is odd, so I make 3n+1: ", end="")
            number = 3 * number + 1
            print(number)
            step += 1
        if lest == 0:
            print(number, end="")
            print(" is even, so I take half: ", end="")
            number = number // 2
            print(number)
            step += 1
    print("It took ", end="")
    print(step, end="")
    print(" steps to reach 1")

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
