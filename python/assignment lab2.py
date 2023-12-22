employee_database=[]
flag=True
while flag==True:
    print("\nemployee Database Menu:")
    print("1. Add new employee")
    print("2. Retrieve employee information")
    print("3. Update available copies")
    print("4. Display all employees")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        employee_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        genre = input("Enter Genre: ")
        available_copies = int(input("Enter Available Copies: "))
    
        employee = {
        'employee ID': employee_id,
        'name': name,
        'age': age,
        'Genre': genre,
        'Available Copies': available_copies
        }
    
        employee_database.append(employee)
        print("employee added successfully. employee ID: {employee_id}")

    elif choice == '2':
        employee_id = input("Enter employee ID: ")
        for employee in employee_database:
          if employee['employee ID'] == employee_id:
            print("employee Information for ID {employee_id}:")
            print("name: {employee['name']}")
            print("age: {employee['age']}")
            print("Genre: {employee['Genre']}")
            print("Available Copies: {employee['Available Copies']}")
            
          else:
            print("employee with ID {employee_id} not found.")

    elif choice=="3":
       employee_id = input("Enter employee ID: ")
       for employee in employee_database:
        if employee['employee ID'] == employee_id:
            new_copies = int(input("Enter new Available Copies: "))
            employee['Available Copies'] = new_copies
            print("Available copies updated for employee ID {employee_id}.")    
       print("employee with ID {employee_id} not found.")

    elif choice=="4":
        print("All employees:")
        for employee in employee_database:
         print("employee ID: {employee['employee ID']}")
         print("name: {employee['name']}")
         print("age: {employee['age']}")
         print("Genre: {employee['Genre']}")
         print("Available Copies: {employee['Available Copies']}")
         print()
      
    elif choice =="5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
