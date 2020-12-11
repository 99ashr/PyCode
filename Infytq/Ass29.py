#!/usr/bin/python3

def calculate(distance,no_of_passengers):
    """Profit calculator for RTC on a bus-route following below conditions 
            fuel_cost is 70rs
            per_ticket_cost=80
            mileage is 10km/litre            """
    profit=0
    ticket_price=80
    mileage=10
    fuel_price=70
    
    
    actual_cost=(distance/mileage)*fuel_price
    print(actual_cost)
    ticket_cost=no_of_passengers*ticket_price
    print(ticket_cost)
    
    if(ticket_cost>actual_cost):
        profit=ticket_cost - actual_cost
        return profit
    else:
        profit=-1
        return profit



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))