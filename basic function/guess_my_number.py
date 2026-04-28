"""
File: guess_my_number.py
Name:Vince
-----------------------------
This program runs a console game
called "Guess My Number".

The program repeatedly asks the user
to guess a number until the correct
answer is given.
"""

# This number controls when to stop the game
SECRET = 32


def main():
    low = 1
    high = 100
    print("Guess an int from 1-100")
    while True:
        guess = int(input("Guess:"))
        if guess == SECRET:
            print("Congrats")
            break
        elif guess > SECRET:
            print("Too high!")
            high = guess
            print(str(low) + "~" + str(high))
        else:
            print("Too low!")
            low = guess
            print(str(low) + "~" + str(high))

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #


if __name__ == '__main__':
    main()
