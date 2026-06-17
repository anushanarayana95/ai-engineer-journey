# Day 9 – File Reading

file = open("Day_09/data.txt", "r")

cities = file.readlines()

file.close()

clean_cities = []

for city in cities:
    clean_cities.append(city.strip().lower())

unique_cities = set(clean_cities)

print("Unique cities from file:", unique_cities)