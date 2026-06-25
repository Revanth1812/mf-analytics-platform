import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Return columns to validate
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert to numeric
for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for missing values after conversion
invalid_returns = df[return_columns].isnull().sum().sum()

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Return Values:", invalid_returns)
print("Invalid Expense Ratio Records:", len(invalid_expense))

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("✅ Cleaned file saved successfully.")