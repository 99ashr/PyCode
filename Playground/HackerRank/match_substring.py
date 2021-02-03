#!/usr/bin/env python3

#! ------------------ Match a substring within another string ----------------- #
string = "ABCDCDC"
substring = "CDC"


def count_substring(string, sub_string):
    """the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

    Args:
        string ([str]): [User defined string]
        sub_string ([str]): [User defined string to match]

    Returns:
        [int]: [Number of matches of substring present within the string]
    """
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(sub_string)] == sub_string:
                count += 1

    return count


print(count_substring(string, substring))
#! ------------------------------------ EOF ----------------------------------- #
