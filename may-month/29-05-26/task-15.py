'''
develop a function that calculates the area and perimeter of a rectangle and returns both values
'''

def rectangle(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter

r = rectangle(10, 20)

print(f"Area: {r[0]}")
print(f"Perimeter: {r[1]}")
