#!/usr/bin/python3

a=40
b=0
space=40
while b<a-1 and a>0:
	print(' '*a+'*'+'*'*b)
	a-=1
	b+=2
for _ in range(4):
	print(' '*(space-1)+'|||')
print(' '*(space-5),'\_@_@_@_/')