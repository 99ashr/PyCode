#!/usr/bin/python3


def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):

    """A Python Program to calculate the bill of the requested gems if there're any otherwise showing -1 if 
        there's no requested gem available"""
    bill_amount=0
    #Write your logic here
    d={}
    for i,j in zip(gems_list,price_list):
        d[i]=j
    # print(d)
    r={}
    for i,j in zip(reqd_gems,reqd_quantity):
        r[i]=j
    # print(r)
    ds=set(d)
    rs=set(r)
    report={}
    
    for a in ds.intersection(rs):
        report[a]=d[a]*r[a]
        
    # print(report)
    repo=set(report)
    if(repo==rs):
        bill_amount=sum(report.values())
        if bill_amount>30000:
            bonus=bill_amount*.05
            bill_amount-=bonus
    else:
        bill_amount=-1
    
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)