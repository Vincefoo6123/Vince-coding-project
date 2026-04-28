"""
File: predicate_function.py
Name:
-------------------------------
This program introduces a predicate
function called is_odd.

The function is_odd(n) returns True
when the number is odd and False
when the number is even.
"""


def main():
    """
    This program tells users if the input number is odd or not
    """
    print("This program tells you if 'a' is an odd number.")
    a = int(input('a: '))
    print(is_odd(a))


def is_odd(n):
    """
    :param n: int
    :return: bool, if n is an odd number or not
    """
    return n % 2 == 1


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
