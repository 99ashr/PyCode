#!/use/bin/Python

#debug the below code
'''counter1=0
counter2=5
star=''
while(counter2>counter1):
  # star=""
  while(counter1 < 5):
     star=star+ "*"
     counter1+=1
     print(star)
counter2-=1'''

n=5
m=5
star=''
for j in range(n):
	print(star)
	for i in range(m):
		print('*',end='')
	m-=1