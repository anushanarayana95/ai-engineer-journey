import csv

employees = []
max_salary = 0
top_employee = ""

with open("Day_11/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)
        salary = int(row["salary"])
# finding highest salary
        if salary > max_salary:
            max_salary = salary
            top_employee = row["name"] 
        
# Sort by salary descending
employees.sort(key=lambda x: int(x["salary"]), reverse=True)

print("Employees sorted by salary (high to low):\n")

for emp in employees:
    print(emp["name"], emp["salary"])
    employees.sort(key=lambda x: int(x["salary"]), reverse=False)

print("Employees sorted by salary (low to high):\n")

for emp in employees:
    print(emp["name"], emp["salary"])

employees.sort(key=lambda y: (y["name"]))
print("Employees sorted by name (A TO Z):\n")

for emp in employees:
    print(emp["name"], emp["salary"], emp["city"])
   
    employees.sort(key=lambda y: (y["name"]), reverse=True)
print("Employees sorted by name (Z TO A):\n")

for emp in employees:
    print(emp["name"], emp["salary"], emp["city"])

print("Highest Salary:", max_salary)
print("Employee:", top_employee)