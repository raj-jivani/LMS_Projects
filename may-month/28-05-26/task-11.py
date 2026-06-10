'''
DEvelop a programme that allows user to pass any combination of attributes for an employee 
(e.g. name, department, salary) using **kwargs 
    - Check if any required fields are missing and print a message accordingly.
'''

def employee_details(**kwargs):
    for key,value in kwargs.items():
        if value == "":
            print(f"{key} is required")
        else:
            print(f"{key} : {value}")

employee_details(name="Raj",age=23,department="")