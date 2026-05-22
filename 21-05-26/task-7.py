'''
write a programme using while loop to:
    - Take numbers as input fromthe user until they entre "0"
'''

while True:
    i = int(input("Entre number: "))
    
    if i == 0:
        print("Programme Stopped")
        break
    print(i)