employee_database=[]
flag=True
while flag==True:
    print("\nemployee Database Menu:")
    print("1. Add new employee")
    print("2. Retrieve employee information")
    print("3. Update employee salary")
    print("4. Display all employees")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        employee_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        position = input("enter the position: ")
        salary = int(input("Enter employee salary: "))
        
        employee = {
        'employee ID': employee_id,
        'name': name,
        'age': age,
        'gender': gender,
        'employee salary': salary
        }
    
        employee_database.append(employee)
        print(f"employee added successfully. employee ID:{employee_id}")

    elif choice == '2':
        employee_id = input("Enter employee ID: ")
        for employee in employee_database:
          if employee['employee ID'] == employee_id:
            print(f"employee Information for ID {employee_id}:")
            print(f"name: {employee['name']}")
            print(f"age: {employee['age']}")
            print(f"gender: {employee['gender']}")
            print(f"employee salary: {employee['employee salary']}")
            
          else:
            print(f"employee with ID {employee_id} not found.")

    elif choice=="3":
       employee_id = input("Enter employee ID: ")
       for employee in employee_database:
        if employee['employee ID'] == employee_id:
            new_copies = int(input("Enter new employee salary: "))
            employee['employee salary'] = new_copies
            print(f"employee salary updated for employee ID {employee_id}.")
        else:    
            print(f"employee with ID {employee_id} not found.")

    elif choice=="4":
        print("All employees:")
        for employee in employee_database:
         print(f"employee ID: {employee['employee ID']}")
         print(f"name: {employee['name']}")
         print(f"age: {employee['age']}")
         print(f"gender: {employee['gender']}")
         print(f"employee salary: {employee['employee salary']}")
         print()
      
    elif choice =="5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
