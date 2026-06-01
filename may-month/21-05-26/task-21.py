'''
write a pyhton programme to print the following pattern right-angled triangle numeric pattern:
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
'''
n = int(input("Number of rows: "))

for i in range(0, n):
    for j in range(i+1,n+1):
        print(j, end=" ")
    print()
    
print("Task END")