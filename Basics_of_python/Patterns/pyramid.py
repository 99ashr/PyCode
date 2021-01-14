n = 10


def pyramid():
    for i in range(1, n+1):
        for _ in range(n-i):
            print(" ", end="")
        for star in range(i):
            print("*", end=" ")
        print()
    return "Pyramid!!!"


pyramid()
