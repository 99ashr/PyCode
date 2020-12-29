def right_half_pyramid(n):
    for i in range(1, n+1):
        for i in range(i):
            print("*", end="")
        print("\r")  # \r --> carriage return


# right_half_pyramid(5)


def pypart(n):
    myList = []
    for i in range(1, n+1):
        myList.append("*"*i)
    print("\n".join(myList))


# Driver Code
n = 5
pypart(n)


def left_half_pyramid(n):
    for i in range(1, n+1):
        for i in range(1, (n+1)-i):
            print(" ", end="")
