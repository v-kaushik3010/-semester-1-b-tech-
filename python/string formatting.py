'''fname = "gla"
lname = "University"
fullname = fname+" "+lname
print(fullname)'''

'''myData = "I like this class"
print(len(myData))'''

'''mytext = "python\"programming\""
print(mytext)'''

'''mytext1 = "Python'programming'"
mytext2 = "python'programming'"'''


'''mytext3 = "     Python Programming    "
print(mytext3.strip())'''


'''mytext4 = "Python Programming"
print(mytext4.upper())
print(mytext4.lower())'''


'''mytext6 = "Python Programming"
print(mytext6.replace("Programming","coding"))'''


'''mytext7 = "My University name is :- GLA "
print(mytext7.find("GLA"))'''


'''mytext8= "hello world"
print(mytext8.capitalize())'''


'''mytext9 = "hello world"
print(mytext9.name())'''


'''mytext10 = "abc"
print(mytext10.isalpha())'''


'''mytext11 = "123"
print(mytext11.isdigit())'''


'''mytext12="Hello World3"
print(mytext12.isupper())
print(mytext12.islower())
print(mytext12.isspace())
print(mytext12.isalnum())'''



#how many alpha,num,space,special in input given by user
'''a= (input("enter your input:::"))
alphabet = 0
num = 0
space = 0 
special=0
length = len(a)
for i in range(0,length):
    if a[i].isalpha():
        alphabet+=1
    elif a[i].isdigit():
        num+=1
    elif a[i].isspace():
        space+=1
    else:
        special+=1
print(alphabet)
print(num)
print(space)
print(special)'''



'''a = input("enter your passwor :::")
upper, lower, num, special = 0,0,0,0
length = len(a)

for i in range(0,length):
    if a[i].isupper():
        upper+=1
    elif a[i].islower():
        lower+=1
    elif a[i].isdigit():
        num+=1
    else:
        special+=1
if (length <12) or (upper<1) or (lower<1) or (num<1) or (special <1):
    print("your password is incorrect")
else:
    print("your password is strong ")'''

    
'''text13 = "hello world ,hello universe"
print (text13.count("hello"))'''

'''words = ['hello','world']
text = ",".join(words)
print (text)'''

'''text14 = "python is awesome"
print(text14[1::2])
print (text14[::3])'''


'''text15= "python is awesome"
input = text15[::-1]
print (input[::3])'''

'''text16 = "welcome the GLA university"
print(text16[slice(10)])
print(text16[slice(0,5)])
print(text16[slice(-7,-1)])'''
#print(text16[slice(-1,-7)]) no output
#print(text16[slice(7,1)]) no output

