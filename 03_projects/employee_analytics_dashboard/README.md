# Employee Analytics Dashboard

## Project Overview

This project analyzes employee salary data using Python and Pandas.

The goal is to extract useful business insights from employee records, including salary statistics, city-wise analysis, and employee distribution.

---

## Dataset

The dataset contains the following fields:

| Column | Description       |
| ------ | ----------------- |
| name   | Employee Name     |
| city   | Employee Location |
| salary | Employee Salary   |

Sample Data:

```text
name,city,salary
Ravi,Chennai,30000
Anu,Mumbai,35000
John,Delhi,40000
Meena,Banglore,45000
Vishnu,Mumbai,50000
Ayra,Banglore,30000
```

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Git
* GitHub

---

## Analysis Performed

### Dataset Inspection

* Loaded CSV data
* Verified data types
* Checked row and column counts

### Salary Analysis

* Highest salary
* Lowest salary
* Average salary
* Top-paid employees

### City Analysis

* Average salary by city
* Employee count by city
* Highest salary by city

### Data Cleaning

* Removed unwanted spaces using:

```python
df["city"] = df["city"].str.strip()
```

---

## Key Results

### Employee Count

```text
6
```

### Highest Salary

```text
50000
```

### Lowest Salary

```text
30000
```

### Average Salary

```text
38333.33
```

### City With Highest Average Salary

```text
Mumbai
```

Average Salary:

```text
42500
```

### Top Paid Employee

```text
Vishnu
```

Salary:

```text
50000
```

---

## Charts Generated

### 1. Average Salary By City

Shows how salaries vary across cities.

File:

```text
charts/salary_by_city.png
```

### 2. Employee Count By City

Shows employee distribution.

File:

```text
charts/employees_by_city.png
```

### 3. Salary Distribution

Shows how salaries are spread across employees.

File:

```text
charts/salary_distribution.png
```

---

## Project Structure

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

---

## Skills Demonstrated

* CSV Handling
* Data Cleaning
* Data Analysis
* GroupBy Operations
* Aggregation Functions
* Data Visualization
* Reporting Insights
* Git & GitHub Workflow

---

## Lessons Learned

* Importance of cleaning data before analysis.
* How to summarize business data using Pandas.
* How to calculate salary statistics.
* How to use GroupBy effectively.
* How to create visual reports using Matplotlib.

---

## Future Improvements

* Add employee departments.
* Add employee experience levels.
* Build interactive dashboards using Streamlit.
* Connect to SQL databases.
* Create automated reports.

---

## Author

Anusha Narayana

AI Engineer Journey Repository
