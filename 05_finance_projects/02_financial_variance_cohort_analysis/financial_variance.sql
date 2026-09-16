-- Synthetic SQL practice for financial reporting and cohort analysis

CREATE TABLE financial_variance (
    month TEXT,
    region TEXT,
    cohort TEXT,
    actual_revenue REAL,
    budget_revenue REAL,
    actual_cogs_pct REAL,
    budget_cogs_pct REAL,
    actual_marketing_pct REAL,
    budget_marketing_pct REAL
);

-- Revenue variance by month
SELECT month,
       SUM(actual_revenue) AS actual_revenue,
       SUM(budget_revenue) AS budget_revenue,
       SUM(actual_revenue - budget_revenue) AS revenue_variance
FROM financial_variance
GROUP BY month
ORDER BY month;

-- Revenue variance by region
SELECT region,
       SUM(actual_revenue) AS actual_revenue,
       SUM(budget_revenue) AS budget_revenue,
       SUM(actual_revenue - budget_revenue) AS revenue_variance
FROM financial_variance
GROUP BY region;

-- Cohort analysis
SELECT cohort,
       SUM(actual_revenue) AS actual_revenue,
       SUM(budget_revenue) AS budget_revenue,
       SUM(actual_revenue - budget_revenue) AS revenue_variance
FROM financial_variance
GROUP BY cohort;

-- Flag material variances at or above 5%
SELECT month, region, cohort,
       actual_revenue - budget_revenue AS revenue_variance,
       ROUND((actual_revenue - budget_revenue) * 100.0 / budget_revenue, 2) AS variance_pct
FROM financial_variance
WHERE ABS((actual_revenue - budget_revenue) * 100.0 / budget_revenue) >= 5
ORDER BY ABS((actual_revenue - budget_revenue) * 100.0 / budget_revenue) DESC;
