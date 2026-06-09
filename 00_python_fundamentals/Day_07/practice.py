# User input employee data and count by city

employees = []

n = int(input("How many employees do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for employee {i+1}")
    
    name = input("Name: ")
    city = input("City: ")
    salary = int(input("Salary: "))

    emp = {
        "name": name,
        "city": city,
        "salary": salary
    }

    employees.append(emp)

# Group by city
city_count = {}

for emp in employees:
    city = emp["city"]

    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nEmployee count by city:\n")

for city, count in city_count.items():
    print(city, ":", count)