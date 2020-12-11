#!/usr/bin/python3


def generate_ticket(airline,source,destination,no_of_passengers):
	"""This python program manages a list of passengers who board flight with their basic details of airline
		source and destination"""

    ticket_number_list=[]

    count=0
    num=101
    while count<no_of_passengers:
        tkt=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(num)
        num+=1
        count+=1
        ticket_number_list.append(tkt)
    
    
    return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))