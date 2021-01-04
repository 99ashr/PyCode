n = 10


def Inverted_right_half_pyramid():
    for i in range(n):
        for j in range(i+1, n+1):
            print('*', end="")
        print()


Inverted_right_half_pyramid()
