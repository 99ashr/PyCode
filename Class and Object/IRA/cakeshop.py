class Cake:
    def init(self,id,price,size,name):
        self.id=id
        self.price=price
        self.size=size
        self.name=name
        

class CakeShop:
    def init(self,cn,CakeList):
        self.cn=cn 
        self.CakeList=CakeList
        
    def fm(self):
        minobj=min(self.CakeList, key=lambda x:x.size)
        return minobj
    
        
    def so(self):
        sortobj=sorted(self.CakeList,key=lambda x:x.price) 
        empl=[]
        for i in sortobj:
            empl.append(i.price)
        if len(empl)==0:
            return None
        else:
            return empl
        
            
n=int(input ())
clist=[]
for i in range (n):
    id=int(input())
    price=int(input())
    size=int(input())
    name=input()
    c=Cake(id,price,size,name)
    clist.append(c)
d=CakeShop("abc",clist)
a=d.fm()
if a== None:
    print("NO Data Found.")
else :
    print (a.id)
    print (a.price)
    print(a.size)
    print(a.name)
    
a2=d.so()
if a2== None:
    print("No Data Found.")
else:
    for i in range(len(a2)):
        print(a2[i])




