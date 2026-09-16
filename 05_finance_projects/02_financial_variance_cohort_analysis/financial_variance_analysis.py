import pandas as pd

# Synthetic data only

df = pd.read_csv("financial_variance_data.csv")

df["revenue_variance"] = df["actual_revenue"] - df["budget_revenue"]
df["revenue_variance_pct"] = (df["revenue_variance"] / df["budget_revenue"] * 100).round(2)
df["gross_profit_actual"] = df["actual_revenue"] * (1 - df["actual_cogs_pct"])
df["gross_profit_budget"] = df["budget_revenue"] * (1 - df["budget_cogs_pct"])
df["gross_profit_variance"] = df["gross_profit_actual"] - df["gross_profit_budget"]

print("Monthly variance:")
print(df[["month", "region", "revenue_variance", "revenue_variance_pct", "gross_profit_variance"]])

region_summary = (
    df.groupby("region")
      .agg(actual_revenue=("actual_revenue", "sum"),
           budget_revenue=("budget_revenue", "sum"),
           gross_profit=("gross_profit_actual", "sum"))
      .reset_index()
)
region_summary["revenue_variance"] = region_summary["actual_revenue"] - region_summary["budget_revenue"]
region_summary["revenue_variance_pct"] = (
    region_summary["revenue_variance"] / region_summary["budget_revenue"] * 100
).round(2)

print("\nRegion summary:")
print(region_summary)

cohort_summary = (
    df.groupby("cohort")
      .agg(actual_revenue=("actual_revenue", "sum"),
           budget_revenue=("budget_revenue", "sum"),
           gross_profit=("gross_profit_actual", "sum"))
      .reset_index()
)
cohort_summary["revenue_variance"] = cohort_summary["actual_revenue"] - cohort_summary["budget_revenue"]
cohort_summary["gross_margin"] = (
    cohort_summary["gross_profit"] / cohort_summary["actual_revenue"] * 100
).round(2)

print("\nCohort summary:")
print(cohort_summary)

material = df[df["revenue_variance_pct"].abs() >= 5]
print("\nMaterial variance items (>=5%):")
print(material[["month", "region", "cohort", "revenue_variance_pct"]])
