import pandas as pd


df = pd.read_csv("/workspaces/ai-engineer-journey/03_projects/employee_analytics_dashboard/employees.csv")
df["city"] = df["city"].str.strip()
print(df)
df.shape
df.info()
df.head()
#Employee Count
print("Employee count:", len(df))
#Highest Salary
print("Highest salary:", df["salary"].max())
#Lowest Salary
print("Lowest salary:", df["salary"].min())
#Average Salary
print("Average salary:", df["salary"].mean())
# Top Paid Employee
print(df.nlargest(1, "salary"))
#Lowest Paid Employee
print(df.nsmallest(1, "salary"))
#Salary by City
city_salary = (
    df.groupby("city")["salary"]
      .mean()
      .reset_index(name="Mean Salary")
)

print("\nMean Salaries By City")
print(city_salary)
#Top 3 Highest Paid Employees
top3 = df.nlargest(3, "salary")

print("\nTop 3 Highest Paid Employees")
print(top3)
#Employee Count by City
employee_city_count = df["city"].value_counts()

print("\nEmployee Count By City")
print(employee_city_count)
# Highest Paid Employee in Each City
city_max = (
    df.groupby("city")["salary"]
      .max()
      .reset_index(name="Highest Salary")
)

print("\nHighest Salary By City")
print(city_max)

#Create Chart 1
import matplotlib.pyplot as plt

city_salary = (
    df.groupby("city")["salary"]
      .mean()
)

plt.figure(figsize=(8,5))

city_salary.plot(kind="bar")

plt.title("Average Salary By City")
plt.xlabel("City")
plt.ylabel("Salary")

plt.tight_layout()

plt.savefig("/workspaces/ai-engineer-journey/03_projects/employee_analytics_dashboard/charts/salary_by_city.png")

plt.close()
 #char Employee Count
plt.figure(figsize=(8,5))

df["city"].value_counts().plot(kind="bar")

plt.title("Employee Count By City")
plt.xlabel("City")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("/workspaces/ai-engineer-journey/03_projects/employee_analytics_dashboard/charts/employees_by_city.png")

plt.close()
# Chart Slary Distribution
plt.figure(figsize=(8,5))

df["salary"].plot(kind="hist")

plt.title("Salary Distribution")
plt.xlabel("Salary")

plt.tight_layout()

plt.savefig("/workspaces/ai-engineer-journey/03_projects/employee_analytics_dashboard/charts/salary_distribution.png")

plt.close()
