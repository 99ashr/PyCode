#!/usr/bin/Python3

""" A Python Program to calculate per head cost amoung four friends and also 
checking the divisibility of the total cost of the trip"""

friends=4
mileage=12
amount_per_litre=65
distance_one_way=96
per_head_cost=0
divisible_by_five=False

#total cost of the trip
total_cost=((2*distance_one_way)/mileage)*amount_per_litre

# print(total_cost)

per_head_cost=total_cost/friends
# print(per_head_cost)

if(per_head_cost%5==0):
    divisible_by_five=True
else:
    divisible_by_five=False


print(per_head_cost)
print(divisible_by_five)