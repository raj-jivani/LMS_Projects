'''
write a programme where a global variable is updated inside a function to keep track of the sum of all numbers entered by the user
'''

total_sum = 0

def sum_of_numbers(*args):
    global total_sum
    for i in args:
        total_sum += i
    
    return total_sum

print(sum_of_numbers(1,34,55,32,12,45))