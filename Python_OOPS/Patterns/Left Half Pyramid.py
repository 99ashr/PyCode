n = 5


def Left_half_pyramid():
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()
    return "Left Half Pyramid!!!"


Left_half_pyramid()
