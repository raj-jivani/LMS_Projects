'''
Create a dictionary:
student = {"name": "Alice", "age": 20, "grade": "A"}
    - Print the keys and values
    - Add a new key "city": "delhi"
    - Update "age" to 21
    - Delete the "grade" key
'''

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student.keys())  # to get all keys
print(student.values())  # to get all values

student["city"] = "Delhi"  # to add new kwy and value
print(student)

student["age"] = 21   # to update the value of key
print(student)

student.pop("grade")  # to delete the key
print(student)