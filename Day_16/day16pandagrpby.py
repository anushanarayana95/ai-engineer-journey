import pandas as pd

data = {
    "name": ["Ravi", "Anu", "John", "Meena", "Ravi", "Anu", "VIshnu"],
    "city": ["Chennai", "Mumbai", "Delhi", "Chennai", "Delhi", "Mumbai", "Banglore"],
    "sales": [200, 150, 300, 400, 250, 100,250]
}

df = pd.DataFrame(data)
df.to_csv("Day_16/sales.csv", index=False)
print("sales.csv created")

df = pd.read_csv("Day_16/sales.csv")
print(df)

city_sales = df.groupby("city")["sales"].sum()
print(city_sales)
summary = df.groupby("city")["sales"].agg(["sum", "mean", "count"])
print(summary)

person_sales = df.groupby("name")["sales"].sum().sort_values(ascending=False)
print(person_sales)