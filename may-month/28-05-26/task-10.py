'''
Implement a function that accepts product details like name, price, and quantity using **kwargs.
    - Return a formatted string showing the total cost of all products.
'''

def totalCost(**kwargs):
    total_cost = 0
    for key,value in kwargs.items():
        name = value["name"]
        price = value["price"]
        quantity = value["quantity"]
        cost = price * quantity
        total_cost += cost
    
    print(f"Toal cost of all products: {total_cost}")


totalCost(product1 = {"name":"apple", "price": 10, "quantity": 20},
          product2 = {"name": "orange", "price": 15, "quantity": 10},
          product3 = {"name": "mango", "price": 50, "quantity": 50})

