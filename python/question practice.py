#Write a Python program that takes an integer n as input and 
#prints the sum of all numbers from 1 to n that are divisible by both 2 and 3. Use a for loop for this task.
'''n = int(input("enter the word:: "))
a=0
b=0
for i in range(1,n):
    if i%6==0:
        b=b+i
        a+=1
        continue
print(b)
if a==0  :
        print("no number divide by 6")'''
 


 #You are given a string sentence containing words separated by spaces
 #. Write a Python program that counts the number of vowels in the sentence and prints the result.

'''b=input("enter your sentence::  ").lower()
count=0
vowel="aeiou"
for char in b:
    if char in vowel:
        count+=1
print(count)'''


#You are given a list of integers. Write a Python program that squares each element of the list and 
#then filters out the even squared numbers. Finally, print the resulting squared and filtered list in a single line.

'''a= (input("enter the series of number seprated by spaces::  ")).split()
c=int(a)
for x in c:
    b= x**2
    if b%2==0:
        d=str(b)
        print("b".joint)
    continue'''        

#takes starting and ending number as input. nad gives output 

'''start = int(input ("enter starting no :::::"))
end= int(input ("enter starting no :::::"))
for i in range(start,end+1):
 if i%6==0:
  print(i,": good student")
  continue
 elif i%3==0:
  print(i,":student")
  continue
 elif i%2==0:
  print(i,":Good ")
  continue
 else:
  print(i,":")
  continue'''


#made a dictionbary and perform the following operations

'''Inventory= {"apple":10,
            "banana":5,
            "orange":8,
            "grape":3}
print(Inventory)

#1. add 2 more apples to inventory 
Inventory["apple"]+=2
print (Inventory)

#check if bnana in inventory print the message accordingly
if "banana" in Inventory.keys():
    print("yes")
else :
print("no")

#reduce the quantity of grapes by 1
Inventory["grape"]-=1
print(Inventory)

#print total no. of items in inventory 
total_item = sum(Inventory.values())
print(total_item)'''

#create a user defined dict and add the total price witout sum function
mydict={}

#get user value for key-value pairs
num_pairs=int(input("enter the number of key_value pairs::"))

for x in range(num_pairs):
    key=input("enter the item:::")
    value=input("enter the price:::")
    mydict[key]= value
print(mydict)
i=0
for i in mydict.values():
    i+=i
    print (i)