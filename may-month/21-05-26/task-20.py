'''
write a python programme to print the floowing right-angled triangle numeric pattern:
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
'''
row = int(input("Number of rows: "))

for i in range(0, row):
    for j in range(row-i,row+1):
        print(j, end=" ")
    print()

print("Task END")