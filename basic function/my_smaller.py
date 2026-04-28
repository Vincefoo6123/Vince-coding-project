"""
File: my_smaller.py
Name:
-------------------------
This program implements a function
called my_smaller that takes two
arguments and returns the smaller
of the two values.
"""


def main():
    """
    Call my_smaller function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)


def my_smaller(n1, n2):
    """
    :param n1:
    :param n2:
    :return:int
    """
    if n1 < n2:
        return n1
    return n2


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
