import csv

with open("Day_12/employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        try:
            name = row[0].strip().title()
            city = row[1].strip().title()
            salary = int(row[2].strip())

            print(name, city, salary)

        except ValueError:
            print("Invalid salary in row:", row)

        except IndexError:
            print("Missing data in row:", row)