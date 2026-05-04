import csv
  
with open("Day_11/employees.csv", "r") as file:
    reader = csv.DictReader(file)

    print("employess from city chennai", "\n")
    
    for row in reader:
        if row["city"].lower() == "chennai":
            print(row["name"], row["salary"], row["city"])
     

