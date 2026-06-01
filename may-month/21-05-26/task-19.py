'''
write a python programme to print the following right-angled triangle numeric pattern:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
row = int(input("Number of rows: "))

for i in range(row,0,-1):
    for j in range(row,i-1,-1):
        print(j, end=" ")
    print()

