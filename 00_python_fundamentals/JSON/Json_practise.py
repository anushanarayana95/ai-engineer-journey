data = {
    "name": "Anu",
    "city": "Nellore",
    "salary": 50000
}

print(data)
print(data["name"])
print(data["city"])
print(data["salary"])
#Nested JSON

employee = {
    "name": "Ravi",
    "address": {
        "city": "Chennai",
        "state": "Tamil Nadu"
    }
}
print(employee["address"])
print(employee["address"]["city"])
# JSON List
employees = {
    "employees": [
        {
            "name": "Ravi",
            "salary": 50000
        },
        {
            "name": "Anu",
            "salary": 60000
        }
    ]
}

print(employees["employees"])
print(employees["employees"][0])
print(employees["employees"][0]["name"])
#Loop Through JSON

for emp in employees["employees"]:
    print(emp["name"], emp["salary"])

#Convert JSON to DataFrame
import pandas as pd

df = pd.DataFrame(employees["employees"])

print(df)
print(employee["address"]["city"])

print(employees["employees"][0]["name"])


