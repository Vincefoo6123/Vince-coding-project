"""
File: longest_line.py
Name:
---------------------------
This program demonstrates how to
find the longest line in the file
romeojuliet.txt using Python.

By reading the file line by line,
we will practice comparing strings
and keeping track of the longest one.
"""

# This constant shows the file path to romeojuliet.txt
FILEPATH = 'text/romeojuliet.txt'


def main():
	with open(FILEPATH, "r") as f:
		count = 0
		for line in f:
			count += 1
			if count == 1:
				longest_line = line
				line_long = len(longest_line)
			else:
				if len(line) > line_long:
					longest_line = line
					line_long = len(longest_line)
		print(longest_line)
	pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
