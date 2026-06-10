import pandas as pd

df = pd.read_csv("/workspaces/ai-engineer-journey/03_projects/eth_price_analysis/ETH_1h.csv")
# Convert Date Column

df["Date"] = pd.to_datetime(
df["Date"],
format="%Y-%m-%d %I-%p"
)

# Make Date the index

df.set_index("Date", inplace=True)

print("\nIndex Type:")
print(type(df.index))

# Highest Price

print("\nHighest ETH Price:")
print(df["High"].max())

# Lowest Price

print("\nLowest ETH Price:")
print(df["Low"].min())

# Average Close Price

print("\nAverage Close Price:")
print(round(df["Close"].mean(), 2))

# Average Volume

print("\nAverage Volume:")
print(round(df["Volume"].mean(), 2))

# Monthly Analysis
monthly_avg = df["Close"].resample("ME").mean()

print("\nMonthly Average Close Price")

print(monthly_avg.head())


#Day Analysis

df["DayOfWeek"] = df.index.day_name()

day_avg = (
df.groupby("DayOfWeek")["Close"]
.mean()
.sort_values()
)

print("\nAverage Close By Day")

print(day_avg)

#Moving Average

df["MA7"] = df["Close"].rolling(7).mean()

print(
df[["Close", "MA7"]]
.tail()
)


#CHART

import matplotlib.pyplot as plt

# Chart 1: ETH Close Price
plt.figure(figsize=(12,5))
df["Close"].plot()
plt.title("ETH Closing Price")
plt.savefig("charts/eth_close_price.png")
plt.close()

#Chart 2: Volume Trend

plt.figure(figsize=(12,5))
df["Volume"].plot()
plt.title("ETH Trading Volume")
plt.savefig("charts/eth_volume.png")
plt.close()

#Chart 3: Average Close by Day of Week

plt.figure(figsize=(8,5))

day_avg = (
    df.groupby("DayOfWeek")["Close"]
    .mean()
)

day_avg.plot(kind="bar")

plt.title("Average Close Price by Day")
plt.tight_layout()

plt.savefig("charts/eth_day_analysis.png")
plt.close()


