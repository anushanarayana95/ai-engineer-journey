import pandas as pd

data = {
    "name": ["  ravi  ", " ANU ", "john", "meena"],
    "email": [
        "RAVI@gmail.com",
        "ANU@gmail.com",
        "JOHN@gmail.com",
        "MEENA@gmail.com"
    ]
}

df = pd.DataFrame(data)

print(df)

df["name"] = df["name"].str.strip()

print(df)
df["name"] = df["name"].str.lower()

print(df)
df["name"] = df["name"].str.title()

print(df)
print(df["email"].str.contains("gmail"))

df["email"] = df["email"].str.replace(
    "gmail.com",
    "company.com"
)

print(df)