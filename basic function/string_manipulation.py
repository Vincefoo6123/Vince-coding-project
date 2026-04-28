"""
File: string_manipulation.py
Name: 
----------------------------
The goal of this program is to change
"stancode" to "stanCode".

Through this example, students will
practice basic string manipulation
using the following steps:
(1) Start with an empty string
(2) Loop over the original string
(3) Build a new string by concatenation
"""


def main():
	s = input("writing...")
	ans = ""
	for i in range(len(s)):
		ch = s[i]
		if i != 4:
			ans += ch
		else:
			ans += "C"
	print(ans)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
