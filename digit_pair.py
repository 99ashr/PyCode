
#Total numbers
#n=int(input("How Many numbers you want to take: "))
n=8
digit_lst=['234','567','321','345','123','110','767','111']
"""for i in range(n):
    digit=input("Enter the three digit number here: ")
        #print('digit: ',digit)
    digit_lst.append(digit)"""
#All Digits
print(digit_lst)
rslt=[]
for i in range(8):
    maxi=int(max(digit_lst[i]))
    #print(maxi)
    mini=int(min(digit_lst[i]))
    #print(mini)
    com=(maxi*11)+(mini*7)
    rslt.append(com)
print(rslt)
temp=[i for i in range(len(rslt)) if not i == rslt.index(rslt[i])]

print(temp)