exit_card = 'n'
chances = 3
current_balance = 69.69


def pin(chances):
    for chances in range(chances):
        pin_card = str(input("Please enter your pin number here: "))
        # pin_card='3111'
        if pin_card == '3110':
            return("\t\tWelcome to our Banking System!!!")
        else:
            print("You've entered the wrong pin number. \n\t\t Please try again here: ")
    else:
        return("You've exceeded the limit to enter the pin number. Try again later!!!")


#! TODO: Break outer loop from inside
# ** Python doesn't support multiple breaking of loops try 'return or refactors'

def check_balance(current_balance):
    return f"your current balance is {current_balance:.2f}"


def withdrawal(current_balance):
    withdrawal_amount = float(
        input("Please enter the amount you want to withdrawal: "))
    if withdrawal_amount > 0:
        if withdrawal_amount > current_balance:
            print("Your amount is greater than your current balance.")
        else:
            current_balance -= withdrawal_amount
            return f"your current balance is {current_balance:.2f}"
    else:
        return "You've entered a wrong amount. Please check and try again."


def pay_in(current_balance):
    pay_amount = float(input("Enter the amount you want to add in...: "))
    if pay_amount > 0:
        current_balance += pay_amount
        return f"Your current account balance is {current_balance:.2f}"


# def terminate():
#     exit_card = input(
#         "Do you want to exit? \n\t\t Press Y for Yes or N for No")


def ATM(exit_card):
    """This program is an implementation of working of ATM"""
    pin(chances)

    while exit_card != 'y' and 'Y' and "yes" and "Yes":
        print("Choose what you want to do from the list given below: \n\t\tPress 1 ----- Check balance \n\t\t Press 2 ----- Withdraw money\n\t\t Press 3 ----- Add money\n\t\t Press 4 -----Exit")
        option = input("Enter your option here: ")
        if option == '1':
            check_balance(current_balance)
        elif option == '2':
            withdrawal(current_balance)
        elif option == '3':
            pay_in(current_balance)
        elif option == '4':
            # TODO:exit
            pass
        else:
            print("You've entered an undesired option.")

        exit_card = input(
            "Do you want to exit? \n\t\t Press Y for Yes or N for No")


ATM(exit_card)
