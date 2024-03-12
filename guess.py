"""
My modifications to the given code:
	
	1) Remember player name
    2) Make the guess between 1-100 only
    3) Add additional information about the number such as close, too close, too high etc...
	
~ Ayus Chatterjee	
"""

import random
import time

def intro():
    print("\nMay I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    time.sleep(.5)
    print("Go ahead. Guess!\n")
    return name

def pick(name):
    guessesTaken = 0
    number = random.randint(1, 100)  # Change the range to 1-100
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess <= 100 and guess >= 1:  # Adjusted range
                guessesTaken += 1
                if guessesTaken < 6:
                    if guess < number:
                        if number - guess <= 5:
                            print("Low, but you're getting close!")
                        else:
                            print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        if guess - number <= 5:
                            print("High, but you're getting close!")
                        else:
                            print("The guess of the number that you have entered is too high")
                if guess == number:
                    break
            elif guess > 100 or guess < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except ValueError:
            print("I don't think that " + enter + " is a number. Sorry!\n")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!\n')
    else:
        print('Nope. The number I was thinking of was ' + str(number))
    return name

name = intro()  # Ask for name only once
while True:
    name = pick(name)  # Update the name
    playagain = input("Do you want to play again? (yes/no/y/n): ").lower()
    while playagain not in ("yes", "y", "no", "n"):
        playagain = input("Invalid input. Please enter 'yes' or 'no' / 'y' or 'n': ").lower()
    if playagain in ("no", "n"):
        break
            
