def A(x):
    return lambda y: x+y


t = A(60)
print(t(9))
