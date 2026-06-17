from datetime import datetime

def dateDifference():
    first_date = input("Enter the first date (YYYY-MM-DD): ")
    last_date = input("Enter the last date (YYYY-MM-DD): ")
    
    d1 = datetime.date(first_date)
    d2 = datetime.date(last_date)
    
    differece = d2 - d1
    
    print(f"Difference between {first_date} and {last_date} is {differece.days} days.")