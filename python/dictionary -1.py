'''students ={"roll no.":23125200033,
           'name':["varun,rahul"]
           ,"eye color":"brown"}'''
'''print(students)
print(len (students))
print(type(students))'''

'''meathod_2= dict(name="varun",salary="100$",age=19)
print(meathod_2)'''


'''check=students .get("name")
print(check)'''

'''my_keys=students.keys()
print(my_keys)'''

'''my_values=students.values()
print(my_values)'''

'''students["year"]=2020
print(students)
                                # or
students.update({"blood group": "B+"})
print(students)


if "year" in students:
    print("key found")

if "brown" in students.values():
    print("value found")'''


'''thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}

#pop("key")
thisdict.pop("model")
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}


#popitem()   delete last key and value
thisdict.popitem()
print("my data",thisdict)'''


'''thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}


del thisdict["model"]
print(thisdict)

del thisdict
print (thisdict)
#it will show an error as whole dict is deleted'''


'''thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}

thisdict.clear()
print (thisdict)'''

#del keyword delete whole dict show it will show an error while clear function clear the data in dict and print an empty dictionary

'''mystudents={
    "stud1":{
        "name":"sachin",
        "year":2004
    },
    "stud2":{
        "name":"laxman",
        "year":2006
    },
    "stud3":{
        "name":"ram",
        "year":2011
    }
}
print(mystudents)

for x in mystudents:
    print(x)

print(mystudents["stud2"]["name"])'''


'''for x,y in mystudents.items():
    print(x,y)

for x in mystudents.keys():
    print(x)

for y in mystudents.values():
    print(y)'''


#problem statement
#you are required to create a program that allows a user to enter the no. of key-values pairs to construct a dictionary

#initialize an empty dictionary
'''mydict={}

#get user value for key-value pairs
num_pairs=int(input("enter the number of key_value pairs::"))

for x in range(num_pairs):
    key=input("enter the key")
    value=input("enter the velue")
    mydict[key]= value
print(mydict)'''



#assignment1 - creating and manipulating dictionary
#problem ststemenrt= create a dictinary named students_scores with the following key and values:
'''students_scores={
    "jhon":80,
    "jane":90,
    "bob":75,
    "alice":95,
}'''

#get user value for key-value pairs
'''num_pairs=int(input("enter the number of key_value pairs::"))

for x in range(num_pairs):
    key=input("enter the key")
    value=input("enter the velue")
    students_scores[key]= value
print(students_scores)'''


'''#perform following operations
#1add a new student,sam ,with score of 80
students_scores["sam"]=80
print (students_scores)

#2 update bob's score to 80
students_scores["bob"]=80
print(students_scores)

#3 remove jane 
del students_scores["jane"]
print(students_scores)
       #or
#students_scores.pop("jane")'''


'''#assignment4
#you are given a list of students and their corresponding grades. print the highest grade withourt using max function 
students_scores={
    "jhon":80,
    "jane":90,
    "bob":75,
    "alice":95,
}
count=0
for x in students_scores.values():
    if x>count:
        count=x

#list comprehension
top_student=[student for student, grade in students_scores.items() if grade==count]

print("highest grsde =",{count})
print("students with the highest grades:{",".join}")'''





#revision questions


'''my_dict={}

#no. of key - value pairs 
group_value=int(input("no. of key value pairs = "))

for i in range (group_value):
    key= input("enter the keyds:: ")
    value= input("enter the value:: ")
    my_dict[key]=value  

    #my_dict.update({key:value})
print(my_dict)'''


