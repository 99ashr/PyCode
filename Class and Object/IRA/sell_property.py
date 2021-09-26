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


#! ------------------------------- sell_property ------------------------------- #
class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_type = property_type
        self.property_value = property_value
        self.max_bid_price = max_bid_price
        # print(self.property_type, self.property_value, self.max_bid_price)


class Tender:
    def __init__(self, buyerName, propertyType, bidPrice):
        self.buyerName = buyerName
        self.propertyType = propertyType
        self.bidPrice = bidPrice
        # print(self.buyerName, self.propertyType, self.bidPrice)


def bidProperty(propertyObj, tenderObj):
    name = []
    for i in propertyObj:
        for j in tenderObj:
            if i.property_type.lower() == j.propertyType:
                a


PropertyList = []
TenderList = []

p = int(input("Total Property count: "))
for i in range(p):
    property_type = input("Type of the property:")
    property_value = int(input("Base price of the property: "))
    max_bid_price = int(input("Maximum biding for the property: "))
    PropertyList.append(Property(property_type, property_value, max_bid_price))

# t=input("Total Tenders issued: ")

# print(PropertyList)
#& ---------------------------------- Objects ---------------------------------- #


# p1 = Property("Land", 25, 50)
# t1 = Tender("Ashish", 3, 48)

#! ------------------------------------ EOF ----------------------------------- #
