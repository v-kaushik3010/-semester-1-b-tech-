# reverse items in a list 
 

l= list(map(int,input("enter your list :::").split()))

#Ist meathod
'''l.reverse()
print(l)'''

#2nd method
'''l1 = l[::-1]
print (l1)'''

#3rd list 
'''i=0
j=len(l)-1
while i<j:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i+=1
    j-=1
print(l)'''

#4th list
i=0
j=len(l)-1
l[i],l[j]=l[j],l[i]
print(l)