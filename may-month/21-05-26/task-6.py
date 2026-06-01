'''
write a Programme to Python to create a menu-driven telecom calling system using the "match case" feature.
    - For Example:
        - Press 1 for English
        - Press 2 for Hindi
        - Press 3 for Gujarati
'''

print("Welcome Raj Telecome World")
print("Press 1 for English language")
print("Press 2 for Hindi language")
print("Press 3 for Gujarati language")

select = input("Select your language: ")

match select:
    case "1":
        print("You have selected English")
    case "2":
        print("You have selected Hindi")
    case "3":
        print("You have selected Gujarati")
    case _:
        print("Invalid Option")

print("Task END")