n = 5


def right_sided_pattern():
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i, n):
            print('*', end="")
        print()
    return "Right Sided Pattern!!!"


right_sided_pattern()
