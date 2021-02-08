#!/usr/bin/env python3
num = 123456
string = 'this is a string'


# * Convert int into str object then follow the same procedure as you do for string

str_num = str(num)
print(str_num[::-1])


str_list = string.split()

print("String Reversed-->", string[::-1])
print("Word Reversed-->", [i for i in str_list[::-1]])
