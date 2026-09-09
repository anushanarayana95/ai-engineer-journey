# Employee Analytics Dashboard

## 📊 Project Overview

This project analyzes employee salary data using **Python and Pandas** to identify salary patterns, employee distribution, and city-level differences.

The goal is to transform raw employee data into clear **business insights and visual reports**.

## Dataset

The dataset contains employee information with the following fields:

| Column   | Description       |
| -------- | ----------------- |
| `name`   | Employee Name     |
| `city`   | Employee Location |
| `salary` | Employee Salary   |

### Sample Data

```text
name,city,salary
Ravi,Chennai,30000
Anu,Mumbai,35000
John,Delhi,40000
Meena,Banglore,45000
Vishnu,Mumbai,50000
Ayra,Banglore,30000
```

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Git
* GitHub

## 🔍 Analysis Performed

### 1. Dataset Inspection

* Loaded employee data from CSV
* Checked row and column counts
* Verified data types

### 2. Salary Analysis

* Calculated highest salary
* Calculated lowest salary
* Calculated average salary
* Identified top-paid employees

### 3. City Analysis

* Calculated average salary by city
* Counted employees by city
* Identified the city with the highest average salary

### 4. Data Cleaning

Removed unwanted spaces from city names using Pandas:

```python
df["city"] = df["city"].str.strip()
```

## 📈 Key Results

| Metric                           |    Result |
| -------------------------------- | --------: |
| Employee Count                   |         6 |
| Highest Salary                   |    50,000 |
| Lowest Salary                    |    30,000 |
| Average Salary                   | 38,333.33 |
| City With Highest Average Salary |    Mumbai |
| Average Salary — Mumbai          |    42,500 |
| Top-Paid Employee                |    Vishnu |
| Top-Paid Employee Salary         |    50,000 |

## 📊 Visualizations

### Average Salary by City

Shows how average salary varies across employee locations.

`charts/salary_by_city.png`

### Employee Count by City

Shows employee distribution across cities.

`charts/employees_by_city.png`

### Salary Distribution

Shows how employee salaries are distributed.

`charts/salary_distribution.png`

## 📁 Project Structure

```text
employee_analytics_dashboard/
│
├── README.md
├── employee_dashboard.py
├── employees.csv
├── insights.md
│
└── charts/
    ├── salary_by_city.png
    ├── employees_by_city.png
    └── salary_distribution.png
```

## 💡 Skills Demonstrated

* CSV data handling
* Data cleaning
* Exploratory data analysis
* Pandas `groupby()` operations
* Aggregation functions
* Salary analysis
* Data visualization
* Reporting and communicating insights
* Git and GitHub workflow

## 🎯 Key Learning

This project helped me practice the complete basic analytics workflow:

**Raw Data → Cleaning → Analysis → Visualization → Business Insights**

It also strengthened my understanding of Pandas, grouping and aggregation, and presenting analytical results clearly.

## 🚀 Future Improvements

* Add employee departments
* Add employee experience levels
* Build an interactive dashboard using Power BI or Streamlit
* Connect the analysis to a SQL database
* Create automated reports

## 👩‍💻 Author

**Anusha Narayana**

Building practical skills in **Data Analytics, Python, SQL, and AI Engineering**.
