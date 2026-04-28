"""
File: replace_keyword.py
Name:Vince
----------------------
This program demonstrates how to
replace an old word with a new word
in a given string by using the
replace() function.
"""


def main():
	old_s = input("old_s:")
	old_w = input("old_w:")
	new_w = input("new_w:")
	ans = replace(old_s, old_w, new_w)
	print(ans)


def replace(old_s, old_w, new_w):
	if old_w in old_s:
		ans = ""
		i = old_s.find(old_w)
		ans += old_s[:i]
		ans += new_w
		ans += old_s[i+len(old_w):]
		return ans
		"#def to be str"
	else:
		return "error"
	pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
