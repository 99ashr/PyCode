n = 10


def Inverted_right_half_pyramid():
    for i in range(n):
        for j in range(i, n):
            print('*', end="")
        print()


Inverted_right_half_pyramid()
