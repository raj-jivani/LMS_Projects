'''
implement a programme to modify a global variable that stores a username.
- Use a function to update the name based on user input
'''
username = ""

def update_username(name):
    global username
    username = name
    return username

user_name = input("Enetr name: ")

print(update_username(user_name))