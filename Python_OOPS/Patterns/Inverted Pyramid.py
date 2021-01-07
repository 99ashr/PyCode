n = 5


def inverted_pyramid():
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        for star in range(n, i, -1):
            print("*", end=" ")
        print()
    return "Inverted pyramid!!!"


inverted_pyramid()
