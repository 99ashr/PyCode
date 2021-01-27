
def display():
    print("This is direct call display!!!")


def display_import():
    print("This is indirect display!!!")


if __name__ == '__main__':
    print("Executed when invoked directly")
    display()
else:
    print("Executed when imported")
    display_import()
