'''
write a recursive function to find the sum of all digits of a given number until a sigle digit number remains.
'''

def sum_of_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        for i in range(num, 1, -1):
            return num + sum_of_numbers(num - 1)

a = 1
print(sum_of_numbers(a))