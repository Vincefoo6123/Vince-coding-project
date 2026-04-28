"""
File: caesar.py
Name:Vince
------------------------------
This program demonstrates the idea of the Caesar cipher.

The user is first asked to enter a number that determines
how much the alphabet should be shifted to form a cipher
table. After that, any input string will be encrypted
using the generated cipher.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    n = int(input("Secret number:"))
    s = input("What's the ciphered string?")
    new_alpha = create_new_alpha(n)
    new_string = decipher(s, new_alpha)
    print("The deciphered string is: "+new_string)
    """
    TODO:
    """


def create_new_alpha(n):
    ans = ""
    ch = ALPHABET[len(ALPHABET) - n:]
    ans += ch
    ans += ALPHABET[:len(ALPHABET) - n]
    return ans


def decipher(s, new_alpha):
    s = s.upper()
    ans2 = ""
    for i in range(len(s)):
        if s[i] not in ALPHABET:
            ans2 += s[i]
        else:
            j = new_alpha.find(s[i])
            ans2 += ALPHABET[j]
    return ans2.upper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
