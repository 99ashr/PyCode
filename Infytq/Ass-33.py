def find_common_characters(msg1,msg2):
"""This is a python program to display the common characters of two strings"""
    common=""
    for i in msg1:
        for j in msg2:
            if i in common:
                continue
            else:
                if i==j:
                    common+=i
    common=common.replace(" ","")
    # print(common)
    rslt=len(common)
    # print(rslt)
    if rslt==0:
        return -1
    else:
        return common

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)