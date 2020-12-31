def make_pretty(func):
    """Any object which implements the special __call__() method is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it.

    Args:
        func ([type]): [description]
    """
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

# * ordinary()
#! I am ordinary


pretty = make_pretty(ordinary)
pretty()
