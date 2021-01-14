
# @ global_variable scope

# a = 100
# def func():
#     print("In function:", a)
# func()

# print("Outside func:", a)

# @ global variable vs local variable
# b = 9
# def func():
#     b = 15
#     print("In function:", b)

# func()
# print("Outside:", b)


# @ change global variable value while used as a *local variable*
# a = 10
# def func():
#     global a
#     a = 15
#     print("In function:", a)

# func()
# print("Outside function:", a)

# @ accessing multiple global variables using global method
a = 12
b = 15
print("Before function call:", a)
print("Before function call:", b)


def func():
    globals()["a"] = 22
    print("In function:", a)
    globals()['b'] = 25
    print("In functions", b)


func()
print("outside function:", a)
print("outside function:", b)
