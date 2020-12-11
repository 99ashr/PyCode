#!/usr/bin/Python3

def find_max(num1,num2):
	"""Python program to find maximum number between two numbers
		*num1 is always lesser than num2
		*number is only of two digits
		*sum of all the digits of the number is multiple of 3
		*number is a multiple of 5
		**display the maximum number with above mentioned conditions"""
	max_num=-1
	#Empty List to store all the numbers b/w num1 and num2
	num_list=[]
	#num1 digit
	c1=len(str(num1))
	#num2 digit
	c2=len(str(num2))
	if num1<num2:
		if c1<=2:
			for i in range(num1,num2+1):
				if len(str(i))<=2:
					if i%3==0 and i%5==0:
						num_list.append(i)
				else:
					break
			if len(num_list)!=0:
				max_num=max(num_list)
			else:
				print("List is empty")
				max_num=-1
		else:
			print("no 2 digit number found")
			max_num=-1
	else:
		print('num1>num2')
		max_num=-1


	# print(num_list)
	return max_num

max_num=find_max(87,81)
print("Maximum Number:",max_num)