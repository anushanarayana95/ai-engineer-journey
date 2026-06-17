import pandas as pd

df = pd.read_csv("/workspaces/ai-engineer-journey/03_projects/csv_data_cleaner/messy_employees.csv")

print(df)
print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isna().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("\nShape After Removing Duplicates:")
print(df.shape)
df["name"] = df["name"].str.strip().str.title()

df["city"] = df["city"].str.strip().str.title()
print(df)

df["salary"] = df["salary"].fillna(
    df["salary"].mean()
)
print(df)
df.to_csv( "/workspaces/ai-engineer-journey/03_projects/csv_data_cleaner/cleaned_employees.csv",index=False)

print("\nFinal Missing Values:")
print(df.isna().sum())

print("\nFinal Shape:")
print(df.shape)

print("\nCleaned Data:")
print(df)