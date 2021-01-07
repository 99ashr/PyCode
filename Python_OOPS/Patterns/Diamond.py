n = 5


def diamond():
    for i in range(1, n+1):
        for _ in range(n-i):
            print(" ", end="")
        for star in range(i):
            print("*", end=" ")
        print()
    for i in range(n):
        for _ in range(i+1):
            print(" ", end="")
        for star in range(n-1, i, -1):
            print("*", end=" ")
        print()
    return "Diamond"


diamond()
