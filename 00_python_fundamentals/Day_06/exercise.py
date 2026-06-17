# Extra String Practice

data = "   ravi kumar,CHENNAI, ₹45,000  "

clean = data.strip()
parts = clean.split(",")

name = parts[0].title()
city = parts[1].title()
salary = parts[2].replace("₹", "").replace(",", "").strip()

print("Name:", name)
print("City:", city)
print("Salary:", salary)