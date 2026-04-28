"""
File: file_reading.py
Name:Vince
---------------------------
This program demonstrates how to
open and read a text file using
Python.

By reading the contents of a file
and printing them out, we will learn
the basics of file input in Python.
"""


def main():
	filepath = "text/JerrySecret1.txt"
	with open(filepath,"r") as f:
		for line in f:
			print(line,end="")
	pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
