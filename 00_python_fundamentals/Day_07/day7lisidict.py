# Day 7 – List of Dictionaries

employees = [
    {"name": "Ravi", "city": "Chennai", "salary": 30000},
    {"name": "Anu", "city": "Mumbai", "salary": 25000},
    {"name": "John", "city": "Delhi", "salary": 40000}
]

for emp in employees:
    print(emp["name"], "|", emp["city"], "|", emp["salary"])