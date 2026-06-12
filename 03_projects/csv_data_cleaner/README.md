# CSV Data Cleaner

## Project Overview

This project demonstrates how to clean messy CSV data using Python and Pandas.

The dataset contains common real-world data quality issues such as:

* Missing values
* Duplicate records
* Extra whitespace
* Inconsistent capitalization

The goal is to transform raw data into a clean and analysis-ready dataset.

---

## Technologies Used

* Python
* Pandas
* Git
* GitHub

---

## Cleaning Operations Performed

### Missing Value Handling

Filled missing salary values using the column mean.

### Duplicate Removal

Removed duplicate employee records.

### Text Standardization

Standardized:

* Employee Names
* City Names

### Whitespace Cleanup

Removed unnecessary leading and trailing spaces.

### Data Export

Saved cleaned data into:

```text
cleaned_employees.csv
```

---

## Project Structure

```text
csv_data_cleaner/
│
├── cleaner.py
├── messy_employees.csv
├── cleaned_employees.csv
├── cleaning_report.md
└── README.md
```

---

## Skills Demonstrated

* Data Cleaning
* Data Validation
* Missing Value Handling
* Duplicate Detection
* String Processing
* CSV Processing
* Pandas DataFrames

---

## Lessons Learned

* Real-world datasets often contain quality issues.
* Data cleaning is essential before analysis.
* Pandas provides powerful tools for cleaning and transformation.
* Well-structured data improves analysis accuracy.

---

## Future Improvements

* Detect outliers
* Validate salary ranges
* Generate automatic cleaning reports
* Process multiple CSV files
* Build a web interface using Streamlit
