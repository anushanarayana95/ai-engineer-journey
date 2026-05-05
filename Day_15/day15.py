import pandas as pd

df = pd.read_csv("/workspaces/ai-engineer-journey/Day_12/employees_clean_v3.csv")

print("First 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())