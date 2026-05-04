import csv

total_salary = 0
count = 0

with open("Day_11/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_salary += int(row["salary"])
        count += 1

average_salary = total_salary / count

print("Total Salary:", total_salary)
print("Average Salary:", average_salary)