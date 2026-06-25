import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction_type values
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount > 0
invalid_amount = df[df["amount_inr"] <= 0]

# Check valid KYC status values
valid_kyc = ["Verified", "Pending", "Rejected"]
invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid Amount Records:", len(invalid_amount))
print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("✅ Cleaned file saved successfully.")