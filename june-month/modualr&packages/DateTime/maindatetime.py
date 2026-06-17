import option1
import option2
import option3


def date_time_operation():
    while True:
        print("\n Date and Time Operations:")
        
        print("- 1. Display current Date and Time.")
        print("- 2. Calcualte difference between two dates.")
        print("- 3. Format Date into custom format.")
        print("- 4. Stopwatch")
        print("- 5. Countdown Timer.")
        print("- 6. Back to Main Menu.")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                print("You selected option 1.")
                
                option1.currentDateAndTime()
            
            case "2":
                print("You selected option 2.")
                
                option2.dateDifference()
                
            case "3":
                print("You selected option 3.")
                
                option3.customDate()