import pandas as pd

df = pd.read_csv("/workspaces/ai-engineer-journey/00_python_fundamentals/Day_12/employees.csv")
print(df.head())
employee_count = df.groupby('city').size()
print(employee_count)
highest_salary = df['salary'].max()
print(f"Highest salary: ${highest_salary:,}")
avg_salary = df.groupby('city')['salary'].mean().reset_index()
avg_salary.columns = ['city', 'AvgSalary']
avg_salary['AvgSalary'] = avg_salary['AvgSalary'].map('${:,.2f}'.format)
print(avg_salary)

top3 = df.nlargest(3, 'salary')[['name', 'city', 'salary']]
print(top3)
df.sort_values("salary", ascending=False)