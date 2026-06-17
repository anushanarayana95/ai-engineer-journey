import pandas as pd

data = {
    "name": ["  ravi  ", " ANU ", "john", None]
}

df = pd.DataFrame(data)
df["name"] = df["name"].str.strip()

print(df)
df["name"] = df["name"].str.title()

print(df)

df["name"] = df["name"].fillna("Unknown")
print(df)