# Day 5 – Functions

def calculate_bonus(salary):
    if salary > 50000:
        return salary * 0.10
    else:
        return salary * 0.05

emp_salary = int(input("Enter salary: "))
bonus = calculate_bonus(emp_salary)
print("Bonus is:", bonus)
print("new salary after bonous:",bonus+emp_salary)