"""
File: change_digit_to_ch.py
Name:Vince
----------------------
The goal of this program is to perform
a simple string transformation.

It takes a string containing both
digits and letters, and converts each
digit into its corresponding uppercase
letter (1 → A, 2 → B, 3 → C, and so on).

For example, the string "123abcab3b2"
will be transformed by replacing the
digits with letters following this
pattern.
"""


def main():
    mystery = '123abcab3b2'
    ans2 = digit_to_ch(mystery)
    print(ans2)  #ABCabcabCbB
    
    s = '11a22b33c'
    print(digit_to_ch(s))  # 'AAaBBbCCc'


def digit_to_ch(string):
    ans = ""
    for ch in string:
        if ch == "1":
            ans += "A"
        elif ch == "2":
            ans += "B"
        elif ch == "3":
            ans += "C"
        else:
            ans += ch
    return ans





if __name__ == '__main__':
    main()