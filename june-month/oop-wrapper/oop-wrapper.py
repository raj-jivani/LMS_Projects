class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Person created with: \nname: {self.name} \nage: {self.age}")

class Employee:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    
    def display(self):
        print(f"Employee created with: \nName: {self.name} \nAge: {self.age} \nID: {self.id} \nSalary: {self.salary}")

class Manager:
    def __init__(self, name, age, id, salary, department):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
        self.department = department
    
    def display(self):
        print(f"Manager created with: \nName: {self.name} \nAge: {self.age} \nID: {self.id} \nSalary: {self.salary} \nDepartment: {self.department}")



while True:
    print("\n --- Python OOP Project: Employee Management System ---")
    
    print("Choose an Operation:")
    print("- 1. Create a Person")
    print("- 2. Create an Employee")
    print("- 3. Create a Manager")
    print("- 4. Show Details")
    print("- 5. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            print("You have selected option 1.")
            
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            
            person = Person(name, age)
            person.display()
        
        case "2":
            print("You have selected option 2.")
            
            employee_name = input("Enter Employee Name: ")
            employee_age = input("Enter Employee Age: ")
            employee_id = int(input("Enter Employee ID: "))
            employee_salary = int(input("Enter Employee Salary: "))
            
            employee = Employee(employee_name, employee_age, employee_id, employee_salary)
            employee.display()
        
        case "3":
            print("You have selected option 3.")
            
            manager_name = input("Enter Manager Name: ")
            manager_age = int(input("Enter Manager Age: "))
            manager_id = int(input("Enter Manager ID: "))
            manager_salary = int(input("Enter Manager Salary: "))
            manager_department = input("Enter Manager Department: ")
            
            manager = Manager(manager_name, manager_age, manager_id, manager_salary, manager_department)
            manager.display()
        
        case "4":
            while True:
                print("You have selected option 4.")
                
                print("Choose details to show:")
                print("- 1. Person")
                print("- 2. Employee")
                print("- 3. Manager")
                print("- 4. Exit")
                
                select = input("Enter your choice: ")
                
                match select:
                    case "1":
                        person.display()
                    
                    case "2":
                        employee.display()
                    
                    case "3":
                        manager.display()
                    
                    case "4":
                        print("Exiting option. Bye....")
                        break
                    
                    case _:
                        print("Invalid Option")
                        break
        
        case "5":
            print("\nExiting Programme, GoodByee.........")
            break
        
        case _:
            print("Invalid Operation")
            break