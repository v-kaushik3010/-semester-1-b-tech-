employee_database=[]
flag=True
while flag==True:
 print("employee Database Menu:")
 print("1. Add new employee")
 print("2. Retrieve employee information")
 print("3. Update available copies")
 print("4. Display all employees")
 print("5. Exit")
 break




choice=int(input("choose option (1-5):: "))

if choice == '1':
 # User input to add a new employee
 employee_id= int(input("enter the employee id  "))
 name= input("enter the name of employee")
 age= input("enter the name of age")
 genre= input("enter the genre of employee")
 available_copies=int(input("enter the no. of avilable copies::"))

 employee = {
        'employee ID': employee_id,
        'name': name,
        'age': age,
        'Genre': genre,
        'Available Copies': available_copies
    }
 employee_database.append(employee)

 print("new employee is successfully added")

elif choice == '2':
 # User input to retrieve employee information
 b= int(input("employee id"))
 print()

elif choice == '3':
 # User input to update available copies
 employee[available_copies]=int(input("enter the updated no. of copies:: "))
 print("")

elif choice == '4':
 # Display information of all employees
 print("4")

elif choice == '5':
  flag=False
  print("Exiting the program.")
