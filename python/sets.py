thisset={"a1","a2","a3"}
print(thisset)

thisset1={"a1","a2","a3","a4","a2"}
print(thisset1)

myset = set(("a1","a2","a3"))
print(myset)


myData={"1","2","3","4","5","6"}
for x in myData:
    print(x,end="")


myset.add(26)
print(myset)

my1 = {1,2,3,4,5}
my2 = {6,7,8,9,10}
my1.update(my2)
print(my1)
d1 = {26,37,78}
d2 = {45,67,88}
d1.update(d2)
print(d1)

d1.remove(67)
print(d1)

d1.discard(88)
print(d1)



d1.pop()
print(d1)

d1.clear()
print(d1)

d1.clear()
print(d1)







































