"""
File: reverse_string.py
Name: 
----------------------------
The goal of this program is to
reverse the string "stressed".

By doing so, we will observe
a fun and interesting result
while practicing string manipulation.
"""


def main():
	"""
	This program reverses 'stressed'
	"""
	old_str = 'stressed'
	new_str = reverse(old_str)
	print('The reversed string of ' + old_str + ' is: ' + new_str)


def reverse(string):
	result = ""
	for i in range(len(string)-1, -1, -1):
		ch = string[i]
		result += ch
	return result
	

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
