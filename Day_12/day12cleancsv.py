import csv

cleaned_rows = []

with open("Day_12/employees.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        name = row[0].strip().title()
        city = row[1].strip().title()
        salary = row[2].strip()

        cleaned_rows.append([name, city, salary])

with open("Day_12/employees_clean_v2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "city", "salary"])
    writer.writerows(cleaned_rows)

print("CSV cleaned using csv module!")