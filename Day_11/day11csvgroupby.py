import csv

city_count = {}

with open("Day_11/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]

        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

print("Employee count by city:\n")

for city, count in city_count.items():
    print(city, ":", count)
    