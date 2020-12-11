#! /usr/bin/python3

def sel_sort(mylist):
	for i in range(len(mylist)):
		k=i
		for j in range(i,len(mylist)):
			if(mylist[j]<mylist[k]):
				k=j
		if(k!=j):
			temp=mylist[i]
			mylist[i]=mylist[k]
			mylist[k]=temp
	print('List after sorting:',mylist)


mylist=[3,6,8,1,9,2,4]
print("List before sorting:",mylist)

sel_sort(mylist)