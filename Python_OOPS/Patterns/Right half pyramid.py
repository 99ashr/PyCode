n = 10


def Right_half_pyramid():
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    return "Right half pyramid"


Right_half_pyramid()
