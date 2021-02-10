#!/usr/bin/env python3


#! ------------------------------- Greatest ------------------------------- #
#Start your code from here!
def Greatest(nums):
    nums.sort()
    print(f"{nums[(len(nums))-1]} is the Greatest of all the given numbers")

nums=[99,23,45,87,56,999,456,245,647,253,76,354,765]

Greatest(nums)


#! ------------------------------------ EOF ----------------------------------- #