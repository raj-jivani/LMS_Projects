'''
create a programe that uses a global variable to count the number of times a specific function called.
'''
count = 0

def count_function():
    global count
    count += 1 
    return count

count_function()
count_function()
count_function()
count_function()
count_function()
count_function()
count_function()
count_function()
count_function()
count_function()

print(f"function called {count} times")