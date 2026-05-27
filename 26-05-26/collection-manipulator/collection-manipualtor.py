all_students = []
all_subjects = set()

while True:
    
    print("Welcome to the Student Data Organizer")
    
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Sudent Information")
    print("4. Delete Student ")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    select_option = input("Entre your choice: ")
    
    match select_option:
        case "1":
            print("You selected option 1")
            print("Entre Student Details:")
            
            student_id = int(input("Entre Student ID: "))
            student_name = input("Entre Student Name: ")
            student_age = int(input("Entre Student Age: "))
            student_grade = input("Enter Student Grade: ")
            student_dob = input("Enter Student's date of birth(YYYY-MM-DD): ")
            student_subjects = input("Enter Student Subjects (comma-seprateed): ")
            
            subjects = set(student_subjects.split(","))
            
            for i in subjects:
                all_subjects.add(i)
            
            
            student = {
                "id": student_id,
                "name": student_name,
                "age": student_age,
                "grade": student_grade,
                "date-of-birth": student_dob,
                "subjects": subjects
            }
            
            all_students.append(student)
            
            print("Student Added Successfully")
        
        case "2":
            print("You have selected option 2")
            print("All students Details are here....")
            print(all_students)
        
        case "3":
            while True:
                print("You have selected option 3")
            
                print("Select to update information of student")
                print("1.Update name")
                print("2. Update age")
                print("3. Update grade")
                print("4. Update date of birth")
                print("5. Update subjects")
                print("6. Exit")
                
                update_choice = input("Select update option: ")
                
                match update_choice:
                    case "1":
                        print("You like to update Student name")
                        
                        id = int(input("Entre Student ID: "))
                        
                        for i in all_students:
                            if i["id"] == id:
                                update_name = input("Entre new name: ")
                                i["name"] = update_name
                                print(i)
                                break
                        else:
                            print("ID is not available")
                        
                    case "2":
                        print("You like to update student age")
                        
                        id = int(input("Enter Student ID: "))
                        
                        for i in all_students:
                            if i["id"] == id:
                                updated_age = int(input("Entre student age: "))
                                i["age"] = updated_age
                                print(i)
                                break
                        else:
                            print("ID is not available")
                    
                    case "3":
                        print("You like to update student grade")
                        
                        id = int(input("Enter Student ID: "))
                        
                        for i in all_students:
                            if i["id"] == id:
                                updated_grade = input("Enter student grade: ")
                                i["grade"] = updated_grade
                                print(i)
                                break
                        else:
                            print("ID is not available")
                            
                    case "4":
                        print("You like to update student date of birth")
                        
                        id = int(input("Enter Student ID: "))
                        
                        for i in all_students:
                            if i["id"] == id:
                                update_dob = input("Enter Student Date of Birth(YYYY-MM-DD): ")
                                i["date-of-birth"] = update_dob
                                print(i)
                                break
                        else:
                            print("ID is not available")
                    
                    case "5":
                        print("You like to update student subjects")
                        
                        id = int(input("Enter Student ID: "))
                        
                        for i in all_students:
                            if i["id"] == id:
                                updated_subjects = input("Enter Student Subjects: ")
                                
                                subjects = set(updated_subjects.split(","))
                                for i in subjects:
                                    all_subjects.add(i)
                                
                                i["subjects"] = subjects
                                print(i)
                                break
                        else:
                            print("ID is not available")
                    
                    case "6":
                        print("Exiting this Choice")
                        break
                    
                    case _:
                        print("Invalid Option")
                        break
        
        case "4":
            print("You have selected option 4")
            
            id = int(input("Enter Student ID: "))
            
            for i in all_students:
                if i["id"] == id:
                    index = all_students.index(i)
                    print(index)
                    all_students.pop(index)
                    break
            else:
                print("ID is not available")
        
        case "5":
            print("You have selected option 5")
            print("All offered subjects:", all_subjects)
            
        case "6":
            print("Exiting the Programme. Goodbye!!!")
            break
        
        case _:
            print("Invalid Option")
            break