# Day 4 – Dictionaries

employee = {
    "name": "Anusha",
    "age": 28,
    "city": "Chennai"
}

print("Employee details:", employee)

employee["salary"] = 35000
print("After adding salary:", employee)

print("\nLooping through dictionary:")
for key, value in employee.items():
    print(key, ":", value)