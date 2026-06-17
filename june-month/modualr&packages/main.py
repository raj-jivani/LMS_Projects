from DateTime import date_time_operation

while True:
    print("\n =================================================================")
    print("\n Welcome to Multi-Utility Toolkit")
    print("\n =================================================================")
    
    print("\n Choose an Option")
    print("- 1. Datetime and Time Operations")
    print("- 2. Mathematical Operations")
    print("- 3. Random Data Generation")
    print("- 4. Generate unique identifiers (UUID)")
    print("- 5. File Operations (Custome Module)")
    print("- 6. Explore Module Attribute (dir())")
    print("- 7. Exit")
    
    print("\n =================================================================")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            print("You have selected option 1.")
            
            date_time_operation()