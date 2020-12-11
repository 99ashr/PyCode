#!/usr/bin/python3

def count_substr(string,part):
	count1=0
	for i in range(len(string)-len(part)+1):
		if string[i: i+len(part)]==part:
			count1+=1

# Another method of finding substring using python method 'count'
	count2=string.count(part)
	print('count1: ',count1,'count2: ',count2)

# count_substr('ccbcbcbc','cbc')
def inputfun():
	string=input("Enter the string here: ")
	part=input("Enter the substring you wanna search in the string: ")
	count_substr(string,part)
inputfun()