"""
File: complement.py
Name: Vince
----------------------------
This program uses string manipulation to solve a real-world
problem: finding the complementary strand of a DNA sequence.

The program provides different DNA sequences as Python strings.
These strings are case-sensitive, and your task is to generate
and output the correct complementary strand for each sequence.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ""
    for i in dna:
        if i == "A":
            ans += "T"
        elif i == "T":
            ans += "A"
        elif i == "C":
            ans += "G"
        elif i == "G":
            ans += "C"
    if ans == "":
        ans = "DNA strand is missing"
        return ans
    else:
        return ans
    pass



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
