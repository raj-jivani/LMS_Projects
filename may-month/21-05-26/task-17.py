'''
write a python programme to print multiplication tables using nested loops for N numbers in this format:
1 * 1 = 1
1 * 2 = 2
    - where N is the user giver number
'''
N = int(input("Entre value of N: "))
n = 1

for i in range(1, N+1):
    print(f"{n} * {i} = {n*i}")

print("Task END")