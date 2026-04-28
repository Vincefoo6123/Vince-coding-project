"""
File: string_score.py
Name:Vince
------------------------------
This program calculates a score for a given string based on
the types of characters it contains.

Digits are worth 1 point, uppercase letters are worth 2 points,
and lowercase letters are worth 3 points. The score() function
iterates through each character in the string, adds up the
corresponding points, and prints the final total score.
"""


def main():
    """
    TODO:
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    ans = 0
    for i in string:
        if i.isdigit():
            ans += 1
        elif i.isupper():
            ans += 2
        elif i.islower():
            ans += 3
    print(ans)

    pass


if __name__ == '__main__':
    main()