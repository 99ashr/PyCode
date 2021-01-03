
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
a = 10


def func():
    global a
    a = 15
    print("In function:", a)


func()
print("Outside function:", a)
