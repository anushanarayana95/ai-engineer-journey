import pandas as pd

data = {
    "name": ["Ravi", "Anu", None, "John"],
    "city": ["Chennai", None, "Delhi", "Mumbai"],
    "salary": [30000, 25000, None, 40000]
}

df = pd.DataFrame(data)

print(df)

#Find missing values
print(df.isna())

#Count missing values

print(df.isna().sum())

# Drop rows with missing values
clean_df = df.dropna()

print(clean_df)

# Fill missing values
df["salary"] = df["salary"].fillna(0)

df["city"] = df["city"].fillna("Unknown")