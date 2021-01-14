n = 5


def left_sided_Pyramid():
    for i in range(1, n+1):
        for _ in range(n-i):
            print(" ", end="")
        for star in range(i):
            print("*", end="")
        print()
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        for star in range(n-i):
            print("*", end="")
        print()
    return "Left sided pyramid"


left_sided_Pyramid()
