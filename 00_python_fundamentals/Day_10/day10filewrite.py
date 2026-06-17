# Day 10 – Write results to file

cities = ["chennai", "mumbai", "delhi", "chennai", "mumbai"]

unique_cities = set(cities)

file = open("Day_10/report.txt", "w")

for city in unique_cities:
    file.write(city + "\n")

file.close()

print("Report generated: report.txt")