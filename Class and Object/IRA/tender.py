class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_type = property_type
        self.property_value = property_value
        self.max_bid_price = max_bid_price


class Tender:
    def __init__(self, buyerName, propertyType, bidPrice):
        self.buyerName = buyerName
        self.propertyType = propertyType
        self.bidPrice = bidPrice


def bidProperty(propertyList, tenderList):
    names = []
    for item in propertyList:  # 3
        obj = None
        bid_price = 0
        for jtem in tenderList:
            if jtem.propertyType.lower() == item.property_type.lower():
                if jtem.bidPrice >= item.property_value and jtem.bidPrice <= item.max_bid_price:
                    if jtem.bidPrice >= bid_price:
                        bid_price = jtem.bidPrice
                        obj = jtem
        if obj is not None:
            names.append(obj.buyerName)
            propertyList.remove(item)  # 4

    if len(names) > 0:
        return names
    else:
        return None


propertyList = []  # 1
tenderList = []
n = eval(input("Total Property count: "))
for i in range(n):
    property_type = input("Type of the property:")
    property_value = eval(input("Base price of the property: "))
    max_bid_price = eval(input("Maximum biding for the property: "))
    propertyList.append(Property(property_type, property_value, max_bid_price))

m = eval(input("Total Tenders issued: "))
for i in range(m):
    buyerName = input("Enter the buyer name: ")
    propertyType = input("Type of the property: ")
    bidPrice = eval(input("Offered price by the buyer: "))
    tenderList.append(Tender(buyerName, propertyType, bidPrice))


# for i in propertyList:
#     print(i.property_type, i.property_value, i.max_bid_price)

finalList = bidProperty(propertyList, tenderList)  # 2
if finalList == None:
    print("property Not found")
else:
    for item in finalList:
        print(item)
for item in propertyList:
    print(item.property_type)
