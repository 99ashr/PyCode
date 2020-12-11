def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
"""This is a python program to display the maximan count of the patients attended in which department"""


    P=patient_medical_speciality_list.count('P')
    O=patient_medical_speciality_list.count('O')
    E=patient_medical_speciality_list.count('E')
    if P>O and P>E:
        return 'Pediatrics'
    elif O>P and O>E:
        return 'Orthopedia'
    elif E>P and E>O:
        return "ENT"

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)