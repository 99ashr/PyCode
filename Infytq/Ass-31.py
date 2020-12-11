def check_palindrome(word):
    """This is a python program to check palindrome of any string or number"""
    status=1
    actual=word
    # print(actual)
    rev=word[::-1]
    # print(rev)
    if(actual==rev):
        return status
    else:
        status=0
        return status
    

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")