'''
write a python programme that:
    - Uses a for loop to print numbers from 1 to 20.
    - skip number divisible by 4 using the continue statement
'''
for i in range(1,21):
    if i % 4 == 0:
        continue
    print(i)

print("Task END")