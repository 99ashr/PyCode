import random

# **INSTRUCTIONS TO THE GAME
instructions = """\t\t\tINSTRUCTIONS!\n\t1) Guess the correct number and win the game.\n\t2) You can set a limit to your guess\n\t3) Only positive number greater than 0 are considered.\n\t\tGood Luck with the Game!!!"""

print(instructions)

# **The Game!!!
# TODO: Convert the game into GUI using python


def guess_the_number(to_be_guessed, guess, chance):
    """This function is a game that gives a winner for every correct guess of a number chosen by the user!!!
    """
    while guess != to_be_guessed:
        chance += 1
        guess = int(input("Enter you guessed number here: "))
        if guess > 0:

            if guess < to_be_guessed:
                print("Oops! your guess is far behind the number.\n Try Again!  ")
            elif guess > to_be_guessed:
                print("Oh! no you've entered a greater number.\nPlease Try  Again! ")
        else:
            print("you've entered an unacceptable value\n\tPlease try again next time.")
    else:
        print("\t\tCongratulations!!!\nyou have won the game in ",
              chance, " chances!!!")


number = int(input("Enter the limit to your guess here: "))
# number = 20
to_be_guessed = int(number*random.random()) + \
    1  # random number is generated here
guess = 0
chance = 0
winner = guess_the_number(to_be_guessed, guess, chance)  # calling function
