
import csv
import os

os.makedirs("Day_12", exist_ok=True)

data = "name,city,salary\nRavi,Chennai,30000\nAnu,Mumbai,25000\nJohn,Delhi,40000\nMeena,Chennai,45000"
with open("Day_12/employees.csv", "w") as file:
    file.write(data)

print("file generated")

with open("Day_12/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
     print(row["name"], row["city"], row["salary"])

rows = []
with open("Day_12/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["name"].lower() == "ravi":
            row["salary"] = str(int(row["salary"]) + 8000)
        rows.append(row)

with open("Day_12/employees_updated.csv", "w", newline="") as file:
    fieldnames = ["name", "city", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)


print("Salary updated and file saved.")