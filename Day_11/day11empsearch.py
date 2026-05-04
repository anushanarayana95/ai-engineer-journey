import csv

search_name = input("Enter employee name to search: ").lower()


with open("Day_11/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["name"].lower() == search_name:
            print("Found:", row)
            found = True
            break

    else:
     print("Employee not found.")