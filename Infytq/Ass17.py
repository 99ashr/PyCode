#!/usr.bin/python3

"""An organization has decided to provide salary hike to its employees based on their job level.
    Employees can be in job levels 3 , 4 or 5"""

def find_new_salary(current_salary,job_level):
    # write your logic here
    
    if job_level==3:
        bonus=current_salary*0.15
        new_salary=current_salary+bonus
    elif job_level==4:
        bonus=current_salary*0.07
        new_salary=current_salary+bonus
    elif job_level==5:
        bonus=current_salary*0.05
        new_salary=current_salary+bonus
    else:
        new_salary=current_salary

    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)