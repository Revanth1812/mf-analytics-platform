-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Fund
SELECT amfi_code, AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top 5 Performing Funds (5-Year Return)
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 6. Average 3-Year Return
SELECT AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance;

-- 7. Number of Funds by Category
SELECT category, COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- 8. Transactions by Payment Mode
SELECT payment_mode, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode;

-- 9. Average Transaction Amount by State
SELECT state, AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;

-- 10. Highest NAV Recorded
SELECT amfi_code, MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC;