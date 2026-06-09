import pandas as pd

data = {
    "name": ["A", "B", None, "D"],
    "score": [80, None, 90, 70]
}

df = pd.DataFrame(data)
# finding missing values
print(df.isna())
#counting missing values
print(df.isna().sum())
#Replace missing score with average score
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

# removing row of missing value
df = df.dropna(subset=["name"])


print(df.isna().sum().sum())  # Should be 0

print(df)
