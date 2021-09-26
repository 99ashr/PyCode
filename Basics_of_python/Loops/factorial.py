# def fact():
#     num = int(input("Enter the number you want to find factorial of : "))
#     factorial = 1
#     if num < 0:
#         print("Please enter a positive number!")
#     elif num == 0:
#         print("Factorial is: ", factorial)
#     else:
#         for i in range(1, num+1):
#             factorial = int(i*factorial)
#         print(factorial)

# fact()


def fact(n):
    if n < 0:
        return "Please enter a positive number! "
    elif n == 0:
        return 1
    else:
        return fact(n-1)*n


n = 5
# n = int(input("Enter the number you want to find factorial of : "))
print(fact(n))
