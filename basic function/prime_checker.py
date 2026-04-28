"""
File: prime_checker.py
Name:Vince
-----------------------
This program asks the user to enter a number and checks whether
the number is a prime number.

When the program starts, it first prints a welcome message to
the console. It then repeatedly prompts the user to enter an
integer greater than 1 and determines whether the number is prime.

The program will stop running when the user enters the EXIT value.
"""

WRONG = -1


def main():
	"""
	TODO:
	"""
	print("Welcome to the prime checker")
	while True:
		number = int(input("n:"))
		if number == WRONG:
			print("Have a good one!")
			break
		if number < 2:
			print(str(number) + " is not a prime number.")
			continue
			'#restart'
		check_number = 2
		times = 0
		while check_number < number:
			if number % check_number != 0:
				check_number += 1
			else:
				times += 1
				print(str(number) + " is not a prime number.")
				break
		if times == 0:
			print(str(number) + " is a prime number.")
	# print("Welcome to the prime checker")
	# number = int(input("n:"))
	# if number == WRONG:
	# 	print("Have a good one!")
	# else:
	# 	check_number = 2
	# 	times = 0
	# 	while check_number < number:
	# 		if number % check_number != 0:
	# 			check_number += 1
	# 		else:
	# 			check_number += 1
	# 			times += 1
	# 	if times == 0:
	# 		print(str(number) + " is a prime number.")
	# 	else:
	# 		print(str(number) + " is not a prime number.")
	# 	while True:
	# 		number = int(input("n:"))
	# 		check_number = 2
	# 		times = 0
	# 		if number == WRONG:
	# 			print("Have a good one!")
	# 		else:
	# 			while check_number < number:
	# 				if number % check_number != 0:
	# 					check_number += 1
	# 				else:
	# 					check_number += 1
	# 					times += 1
	# 			if times == 0:
	# 				print(str(number) + " is a prime number.")
	# 			else:
	# 				print(str(number) + " is not a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
