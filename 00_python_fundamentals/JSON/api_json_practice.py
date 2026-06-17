import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print(type(data))
print("Total Users:", len(data))

print("\nFirst User:")
print(data[0])
print("\nFirst User Name:")
print(data[0]["name"])

print("\nFirst User Email:")
print(data[0]["email"])
print("\nAll Users")

for user in data:
    print(user["name"])
print(type(data))
print("Total Users:", len(data))
print("\nFirst User Name:")
print(data[0]["name"])

print(data[0].keys())

print(data[0]["address"])
print(data[0]["address"]["city"])
print(data[0]["company"]["name"])


# Convert API Data to DataFrame

import pandas as pd

users = []

for user in data:

    users.append({
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"],
        "company": user["company"]["name"]
    })

df = pd.DataFrame(users)

print(df.head())

print(data[0]["address"]["city"])
print(data[0]["company"]["name"])

df.head()

print(df.shape)

print(df.columns)

print(df["city"].value_counts())

print()

print("Unique Cities:")
print(df["city"].nunique())

print()

print("Unique Companies:")
print(df["company"].nunique())

df.to_csv("/workspaces/ai-engineer-journey/00_python_fundamentals/JSON/users_api_data.csv", index=False)

print("CSV Saved Successfully")
print(df.shape)
print(df["city"].value_counts())
print(df["city"].nunique())
print(df["company"].nunique())

print(df.sort_values("name"))

print(df["company"].sort_values())
df.to_csv("/workspaces/ai-engineer-journey/00_python_fundamentals/JSON/users_api_data.csv", index=False)

print("File saved successfully")
print(df.head())