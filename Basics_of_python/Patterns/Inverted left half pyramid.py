n = 5


def inverted_left_half_pyramid():
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
        for star in range(n-i):
            print("*", end="")
        print()
    return "Inverted left half pyramid!!!"


inverted_left_half_pyramid()
