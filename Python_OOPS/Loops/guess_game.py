import random


def guess_the_number(to_be_guessed, guess):
    """This function is a game that gives a winner for every correct guess of a number chosen by the user!!!
    """
    # print(number, " ", to_be_guessed)
    while guess != to_be_guessed:
        guess = int(input("Enter you guessed number here: "))
        if guess < to_be_guessed:
            print("Oops! your guess is far behind the number.\n Try Again! ")
        elif guess > to_be_guessed:
            print("Oh! no you've entered a greater number.\nPlease Try Again! ")
        else:
            print("Wow you have won the game!!!")


number = int(input("Enter the limit to your guess here: "))
# number = 20
to_be_guessed = int(number*random.random()) + \
    1  # random number is generated here
guess = 0

winner = guess_the_number(to_be_guessed, guess)  # calling function
