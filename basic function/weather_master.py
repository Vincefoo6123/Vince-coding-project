"""
File: weather_master.py
Name:Vince
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""

wrong = -1


def main():
	"""
	compare to the latest data to check which is the highest and the lowest
	two boxes also set boxes to let total/days
	"""
	print("stanCode\"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or "+str(wrong)+" to quit)?"))
	total = 0
	if data < 16:
		cold_day = 1
	else:
		cold_day = 0
	if data == wrong:
		print("No temperatures were entered")
	else:
		maximum = data
		minimum = data
		total += data
		day = 1
		while True:
			data = int(input("Next Temperature: (or -100 to quit)?"))
			if data == wrong:
				break
			elif data > maximum:
				if data < 16:
					cold_day += 1
				total += data
				maximum = data
				day += 1
			elif data < minimum:
				if data < 16:
					cold_day += 1
				total += data
				minimum = data
				day += 1
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = "+str(total/day))
		print(str(cold_day)+" cold day(s)")
	pass


# DO NOT EDIT CODE BELOW THIS LINE #print("Highest temperature = " + str(data))

if __name__ == "__main__":
	main()
