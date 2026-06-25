import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and Date
df = df.sort_values(by=["amfi_code", "date"])

# Forward fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

# Save cleaned file
df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("Cleaned Shape:", df.shape)
print("✅ Cleaned file saved successfully.")