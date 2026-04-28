"""
File: average_2_nums.py
Name: Jerry Liao
------------------------
This program demonstrates functions
with and without parameters, as well
as functions that return values.

The function intro() has neither
parameters nor a return value, while
my_average(a, b) takes parameters
and returns a result.
"""


def main():
    """
    This program prints the average of 10 and 9 on Console
    """
    intro()
    print('The average is: '+str(my_average(10, 9)))


def intro():
    """
    This function wraps 3 prints as intro()
    (Just like what move() does in Karel Program)
    """
    print('Hello! Welcome!')
    print('This program averages 10 and 9')
    print('Have fun!')


def my_average(a, b):
    """
    :param a: int, the first number to be averaged
    :param b: int, the second number to be averaged
    :return ans: float, the average between a and b
    """
    ans = (a+b)/2
    return ans


if __name__ == '__main__':
    main()
