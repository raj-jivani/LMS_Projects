from datetime import datetime

def customDate():
    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    date = input("Enter date (DD): ")
    
    custm_date = datetime.date(year, month, date)
    
    print(f"You custome date is {custm_date}")
