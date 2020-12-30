def user_input():
    """This method takes the filename by the user which will be used later in other methods
    """
    print("\t\tUser Input function!!")
    filename = input("Enter the name of the file here: ")
    return filename


def open_file(filename):
    """This method is opening the file that has been passed by the user!!!

    Args:
        filename ([string]): [description]
    """
    print("\t\t\topen_file function")
    m = input("Press 'w' to write and 'r' for read: ")
    file = open(filename, m)
    print("\t\tFile is opened by this function!!!")
    return (file, m)


def user_input_write_file():
    file_content = input("Enter the content to the file: ")
    return file_content


def read_file(file):
    print(file.read())


def write_file(file):
    file.write(user_input_write_file())


def close_file(file):
    """This function is called to close the file!!!
    """
    file.close()


def handel():
    """This function contains all the file handeling operations!!!
    """
    print("\t\t\tMain function")
    filename = user_input()
    r = open_file(filename)
    file = r[0]
    m = r[1]
    # print(m)
    if m == 'r':
        read_file(file)
    elif m == 'w':
        write_file(file)

    close_file(file)


handel()
