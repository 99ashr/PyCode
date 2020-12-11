#!/usr/bin/python3

def solve(heads,legs):

    """This python program counts the number of rabbits and chicken using the data of head and legs"""

    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    if heads>legs:
        print(error_msg)
    else:    
        if legs%2==0:
            if(heads*2==legs):
                chicken_count=heads
                rabbit_count=0
            elif(heads*4==legs):
                chicken_count=0
                rabbit_count=heads
            else:
                chicken_count=heads
                temp_legs=heads*2
                for i in range(0,heads-1):
                    chicken_count-=1
                    rabbit_count+=1
                    temp_legs+=2
                    if(temp_legs==legs):
                        break
            print(chicken_count,rabbit_count)
            
        else:
            print(error_msg)

    
#Provide different values for heads and legs and test your program
solve(20,10)