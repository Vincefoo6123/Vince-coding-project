"""
File: checkerboard.py
Name:
------------------------
This program prints an alternating
checkerboard pattern to the console
using nested for loops.
"""

# These constants control the size of the checkerboard
ROW = 5  # The number of rows
COL = 8  # The number of cols


def main():
	for i in range(ROW):
		for j in range(COL):
			if(i+j) % 2 == 0:
				print("A", end="")
			else:
				print("*", end="")
		print("")
	pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
