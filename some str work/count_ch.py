"""
File: count_ch.py
Name:
----------------------
The goal of this program is to count
the number of uppercase letters in
different words: 'ApPLE', 'Jerry', and 'PineApple'.

It defines a function called
num_upper() to perform the counting.
This function is then used to count
the uppercase letters in several
example words and print the results.
"""


def main():
    s = 'ApPLE'
    s2 = 'Jerry'
    s3 = 'PineApple'
    print(num_upper(s))
    print(num_upper(s2))
    print(num_upper(s3))


def num_upper(s4):
    count_s = 0
    for i in range(len(s4)):
        if s4[i].isupper():
            count_s += 1
        else:
            pass
    return count_s


if __name__ == '__main__':
    main()