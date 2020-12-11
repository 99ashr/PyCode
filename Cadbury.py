len1=int(input("Min Length: "))
len2=int(input("Max Length: "))
wid1=int(input("Min Width: "))
wid2=int(input("Max Width: "))
count=0
for i in range(len1,len2+1):
    for j in range(wid1,wid2+1):
        l=i
        w=j
        print(l,w)
        while(True):
            if(l==w):
                count+=1
                break
            elif(l<w):
                w-=1
                count+=1
            else:
                l-=w
                count+=1
print(count)