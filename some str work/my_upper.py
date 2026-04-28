"""
File: my_upper.py
Name:
----------------------
This program demonstrates how the
Python built-in method s.upper()
can be implemented.

By recreating its behavior step by
step, we will better understand how
string methods work internally.
"""


def main():
	s = '123JeRrY123'
	print(put_upper(s))


def put_upper(s):
	res = ""
	for i in range(len(s)):
		if s[i].islower():
			res += s[i].upper()
		else:
			res += s[i]
	return res


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
