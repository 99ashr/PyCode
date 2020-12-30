def open_file(filename):
    print("\t\tIn the open_file function")
    # file=open(filename,mode)
    file = open(filename, "r")
    print("\t\tFile is opened by this function!!!")
    file.close()


def handel():
    """This function contains all the file handeling operations!!!
    """
    print("\t\tMain function")
    open_file("./demo_file.txt")


handel()
