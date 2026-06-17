# Day 12 – Manual CSV Cleaning

with open("Day_12/employees.csv", "r") as file:
    lines = file.readlines()

cleaned = []

for line in lines[1:]:
    parts = line.strip().split(",")

    name = parts[0].strip().title()
    city = parts[1].strip().title()
    salary = parts[2].strip()

    cleaned.append(f"{name},{city},{salary}\n")

with open("Day_12/employees_clean.csv", "w") as file:
    file.write("name,city,salary\n")
    file.writelines(cleaned)

print("Manual cleaning done!")