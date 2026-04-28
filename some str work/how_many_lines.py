"""
File: how_many_lines.py
Name:
---------------------------
This program demonstrates how to
calculate the number of lines in
the file romeojuliet.txt.

By reading the file line by line,
we will practice basic file input
and counting techniques in Python.
"""

# This constant shows the file path to romeojuliet.txt
FILEPATH = 'text/romeojuliet.txt'


def main():
	"""
	This program prints the number of
	lines in romeojuliet.txt on Console
	"""
	count = 0
	with open(FILEPATH, 'r') as f:
		for _ in f:
			count += 1
	print('There are ' + str(count) + ' lines in '+str(FILEPATH))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
