def user_input():
    """This method takes the filename by the user which will be used later in other methods
    """
    filename = input("Enter the name of the file here: ")
    return filename


def open_file(filename):
    """This method is opening the file that has been passed by the user!!!

    Args:
        filename ([string]): [description]
    """
    print("\t\tIn the open_file function")
    # file=open(filename,mode)
    file = open(filename, "r")
    print("\t\tFile is opened by this function!!!")
    return file


def close_file(file):
    """This function is called to close the file!!!
    """


def handel():
    """This function contains all the file handeling operations!!!
    """
    print("\t\tMain function")
    open_file("./demo_file.txt")


handel()
