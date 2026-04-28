"""
File: receipt.py
Name:Vince
-------------------------
This program calculates the total cost
of a meal and prints the result to the
console.

Through this program, we will practice
using variables, taking user input, and
combining values into a single output
message.
"""


def main():
    meal = int(input('How much was your meal?'))
    tax = float(input('Tax:'))
    total = meal*(1+tax)
    print('Total:'+str(total)+'!')



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
