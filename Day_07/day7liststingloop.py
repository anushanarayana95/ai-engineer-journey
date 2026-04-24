records = ["  ravi,CHENNAI,30000 ",
    " anu,Mumbai,25000 ",
    " JOHN,delhi,40000 "]

for record in records:
    clean = record.strip()
    parts = clean.split(",")

    name = parts[0].title()
    city = parts[1].title()
    salary = parts[2]

    print("Name:", name, "| City:", city, "| Salary:", salary)