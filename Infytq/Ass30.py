def encode(message):
	emsg=""
	count=1
	for i in range(len(message)):
		j=i+1
		if message[i]==message[j]:
			count+=1
		# elif j>len(message):
		# 	print("Array out of index")
		else:
			emsg+=str(count)+message[i]
			count=1
	print(emsg)


encoded_message=encode('ABBBBCCCCCCCCAB')
print(encoded_message)