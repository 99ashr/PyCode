# Copyright 2021 gaura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#!/usr/bin/env python3


#! ------------------------------- Patient ------------------------------- #
# Start your code from here!
class Patient:
    def __init__(self, Code, Name, Age, DoctorName, BillAmount):
        self.Code = Code
        self.Name = Name
        self.Age = Age
        self.DoctorName = DoctorName
        self.BillAmount = BillAmount


class Doctor:

    def __init__(self, PtList):
        self.PtList = PtList

    def findPatentwithMaxAge(self):
        max_age = 0
        pt_code = None
        for i in PtList:
            if i.Age > max_age:
                max_age = i.Age
                pt_code = i.Code

        if max_age == 0:
            print("No Patient Found!!!")
        else:
            for i in PtList:
                if i.Code == pt_code:
                    print(i.Code)
                    print(i.Name)
                    print(i.Age)
                    print(i.DoctorName)
                    print(i.BillAmount)

    def sortPatientByBillAmount(self):
        s_bill = []
        for i in PtList:
            s_bill.append(i.BillAmount)
        print(s_bill)
        s_bill.sort()
        print(s_bill)


PtList = []
p = int(input("Enter total number of patients: "))
for i in range(p):
    Code = input("Code Name: ")
    Name = input("Patient Name: ")
    Age = int(input("Age: "))
    DoctorName = input("Doctor Name: ")
    BillAmount = float(input("Bill Amount: "))
    PtList.append(Patient(Code, Name, Age, DoctorName, BillAmount))

Doctor.findPatentwithMaxAge(PtList)
Doctor.sortPatientByBillAmount(PtList)
#! ------------------------------------ EOF ----------------------------------- #
