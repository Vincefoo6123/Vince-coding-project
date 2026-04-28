"""
File: quadratic_solver.py
Name:Vince
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math


def main():
	"""
	i use 判別式 to check how many roots in the answer
	then print out the answer
	"""
	for i in range(3):
		print("stanCode Quadratic Solver!")
		a = int(input("Enter a:"))
		b = int(input("Enter b:"))
		c = int(input("Enter c:"))
		if b*b-4*a*c > 0:
			answer1 = (math.sqrt(b * b - 4 * a * c) - b) / 2 / a
			answer2 = (- math.sqrt(b * b - 4 * a * c) - b) / 2 / a
			print("Two roots:", end="")
			print(answer1, end="")
			print(",", end="")
			print(answer2)
		elif b*b-4*a*c == 0:
			print("One root:", end="")
			answer1 = (math.sqrt(b * b - 4 * a * c) - b) / 2 / a
			print(answer1)
		elif b*b-4*a*c < 0:
			print("No roots")

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
