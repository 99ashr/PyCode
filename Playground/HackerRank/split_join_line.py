#!/usr/bin/env python3

#! ------------------- a string can be split on a delimiter. ------------------ #

def split_and_join(line):
    """You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 

    Args:
        line ([string]): [User provided string to be splitted and joined later.]

    Returns:
        [string]: [Hypen separated String]
    """
    a = line
    a = a.split(" ")
    a = "-".join(a)
    return (a)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#! ------------------------------------ EOF ----------------------------------- #
