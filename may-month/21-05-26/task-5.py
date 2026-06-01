'''
write a Programme in Python to create a menu -driven fast-food order system using the 'match-case' feature.
    -For Example:
        - Press 1 to order a sandwich
        - Press 2 to order a pizza
        - Press 3 to order a burger
    - Extend this programme by adding a nested match case for each menu item's subtype selection by the user.
    - For example:
        - Press 1 for thin crust pizza
        - Press 2 for chesse burst pizza
        - Press 3 Fresh dough pizza
'''

print("Welcome to our Rstaurant")
print("Press 1 to order a Sandwich")
print("Press 2 to order a Burger")
print("Press 3 to order a Pizza")

option = input("Select your food item: ")

match option:
    case "1":
        print("You want to order Sandwich")
        print("Now it's time to select sub-type of your food")
        print("Press 1 for veg cheese sandwich")
        print("Press 2 for veg grilled sandwich")
        print("Press 3 for bread butter")
        
        subtype = input("Select any option from above: ")
        
        match subtype:
            case "1":
                print("You ordered a veg cheese sandwich")
            case "2":
                print("You ordered a veg grilled sandwich")
            case "3":
                print("You ordered a bread butter")
            case _:
                print("Invalid choice")
    case "2":
        print("You want to order Burger")
        print("Now it's time to select sub-type of your food")
        print("Press 1 for veg cheese burger")
        print("Press 2 for maharaja burger")
        print("Press 3 for aloo ticky burger")
        
        subtype = input("Select any option from above: ")
        
        match subtype:
            case "1":
                print("You ordered a veg cheese burger")
            case "2":
                print("You ordered a maharaja burger")
            case "3":
                print("You ordered a aloo ticky burger")
            case _:
                print("Invalid choice")
    case "3":
        print("You want to order Pizza")
        print("Now it's time to select sub-type of your food")
        print("Press 1 for Thin Crust Pizza")
        print("Press 2 for Cheese Burst Pizza")
        print("Press 3 for Fresh Dough Pizza")
        
        subtype = input("Select any option from above: ")
        
        match subtype:
            case "1":
                print("You ordered a Thin Crust Pizza")
            case "2":
                print("You ordered a Cheese Burst Pizza")
            case "3":
                print("You ordered a Fresh Dough Pizza")
            case _:
                print("Invalid choice")
    case _:
        print("Invalid Option")

print("Task END")