data = "name,city,salary\nRavi,Chennai,30000\nAnu,Mumbai,25000\nJohn,Delhi,40000\nMeena,Chennai,45000"
file = open("Day_11/employees.csv", "w")
for d in data:
    file.write(d)

file.close()
print("file generated")

import csv

with open("Day_11/employees.csv", "r") as file:
    
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["city"], row["salary"])