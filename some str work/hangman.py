"""
File: hangman.py
Name: Vince
-----------------------------
This program plays a console-based Hangman game.

The user is shown a word represented by dashes and tries to
guess the hidden word by entering one character in each round.
If the guessed character is correct, the program updates and
displays the word on the console.

The player has a limited number of chances, defined by
N_TURNS, to successfully guess the word and win the game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    executes the main logic for the Hangman guessing game.

    This function initializes the game state by retrieving a random word,
    setting the player's lives to 7, and generating a hidden string of dashes.
    It continuously prompts the user for a single alphabetical character,
    validates the input format, and updates the word's visibility based on
    correct guesses.

    The game loop terminates under two conditions:
    1. Win: The player successfully reveals all characters in the word.
    2. Loss: The player's lives reach zero.

    Upon termination, the function displays the final game result and
    reveals the correct answer.
    """
    life = 7
    word = random_word()
    long = len(word)
    ans = "-"*len(word)
    print("The word looks like:" + ans)
    print("You have " + str(life) + " wrong guesses left.")
    while life > 0:
        while True:
            guess = input("Your guess:")
            if not guess.isalpha() or len(guess) != 1:
                print("Illegal format.")
            else:
                guess = guess.upper()
                break
        new_ans = ""
        correct_number = 0
        for i in range(long):
            if word[i] == guess:
                new_ans += word[i]
                correct_number += 1
            else:
                new_ans += ans[i]
        ans = new_ans
        # Use a new string to overwrite 'ans' because strings in Python are immutable
        if correct_number > 0:
            print("You are correct!")
        else:
            print("There is no " + guess + "'s in the word.")
            life -= 1
        if ans == word:
            print("You win!!")
            print("The answer is:" + ans)
            break
        else:
            print("The word looks like:" + new_ans)
            print("You have " + str(life) + " wrong guesses left.")
    if life == 0:
        print('You are completely hung:(')
        print("The answer is:" + word)



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
