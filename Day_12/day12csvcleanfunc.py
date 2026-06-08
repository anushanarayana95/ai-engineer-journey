import csv

def clean_row(row):
    try:
        name = row[0].strip().title()
        city = row[1].strip().title()
        salary = int(row[2].strip())
        return [name, city, salary]
    except:
        return None

cleaned_rows = []

with open("Day_12/employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        cleaned = clean_row(row)
        if cleaned:
            cleaned_rows.append(cleaned)

with open("Day_12/employees_clean_v3.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "city", "salary"])
    writer.writerows(cleaned_rows)

print("CSV cleaned using functions!")