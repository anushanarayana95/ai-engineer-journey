# ETH Price Analysis Insights

## Dataset Overview

* Total Records: 23,674
* Dataset Type: Ethereum Hourly Price Data
* Columns:

  * Date
  * Symbol
  * Open
  * High
  * Low
  * Close
  * Volume

---

## Key Findings

### Highest ETH Price

**Value:** 1419.96 USD

Observation:

Ethereum reached a maximum recorded price of **$1,419.96** during the analyzed period, demonstrating substantial growth potential within the cryptocurrency market.

---

### Lowest ETH Price

**Value:** 80.60 USD

Observation:

The lowest recorded ETH price was **$80.60**. The large gap between the lowest and highest prices highlights the significant volatility of cryptocurrency assets.

---

### Average Close Price

**Value:** 324.93 USD

Observation:

Across the entire dataset, Ethereum's average closing price was approximately **$324.93**.

---

### Day of Week Analysis

| Day       | Average Close Price |
| --------- | ------------------: |
| Saturday  |              327.71 |
| Sunday    |              326.32 |
| Monday    |              326.19 |
| Tuesday   |              325.19 |
| Wednesday |              324.62 |
| Thursday  |              323.33 |
| Friday    |              321.13 |

### Best Performing Day

**Saturday**

Observation:

Saturday had the highest average closing price (**$327.71**), while Friday had the lowest (**$321.13**).

Although the differences are relatively small, the data suggests ETH performed slightly better on weekends during this period.

---

### Moving Average Analysis

Observation:

The 7-period moving average smoothed out short-term price fluctuations and made overall trends easier to identify.

Benefits:

* Reduces noise
* Highlights trends
* Commonly used in trading and financial analysis

---

### Volatility Observation

Ethereum's price ranged from:

```text
$80.60 → $1419.96
```

This represents a difference of:

```text
$1339.36
```

This wide range demonstrates how volatile cryptocurrency markets can be.

---

## Technical Skills Practiced

* CSV data loading with Pandas
* Datetime conversion
* DatetimeIndex creation
* Time-series analysis
* GroupBy operations
* Resampling
* Rolling averages
* Data visualization using Matplotlib

---

## Challenges Faced

### Datetime Parsing Error

Issue:

```text
Unknown datetime string format
```

Solution:

```python
pd.to_datetime(
    df["Date"],
    format="%Y-%m-%d %I-%p"
)
```

---

### DatetimeIndex Error

Issue:

```text
Only valid with DatetimeIndex
```

Solution:

```python
df.set_index("Date", inplace=True)
```

---

## What I Learned

* Time-series analysis requires proper datetime handling.
* Resampling helps analyze data at different time intervals.
* GroupBy can uncover hidden patterns.
* Rolling averages are useful for trend analysis.
* Visualization makes insights easier to communicate.
* Debugging data issues is a critical skill in data analysis.

---

## Future Improvements

* Add 30-day moving average
* Compare ETH and BTC performance
* Build an interactive dashboard
* Fetch live crypto data using APIs
* Create automated reports
