import pandas as pd

data = {
    "name": ["Ravi", "Anu", "John"],
    "joining_date": [
        "2024-01-10",
        "2025-03-15",
        "2023-11-20"
    ]
}

df = pd.DataFrame(data)

print("Before conversion:")
print(df)
print(df.dtypes)

# Convert to datetime
df["joining_date"] = pd.to_datetime(df["joining_date"])

print("\nAfter conversion:")
print(df.dtypes)

# Extract date parts
df["year"] = df["joining_date"].dt.year
df["month"] = df["joining_date"].dt.month
df["day"] = df["joining_date"].dt.day
df["day_name"] = df["joining_date"].dt.day_name()

print("\nFinal DataFrame:")
print(df)

print("\nEmployees joined in 2025:")
print(df[df["year"] == 2025])
print ("\n employees joined on month 11:")
print(df[df["month"] == 11])
print("\n joined on Saturday:")
print(df[df["day_name"] == "Saturday"])