import pandas as pd

# Read fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("Unique Fund Houses")
print(df["fund_house"].unique())

print("\n" + "=" * 60)
print("Unique Categories")
print(df["category"].unique())

print("\n" + "=" * 60)
print("Unique Sub Categories")
print(df["sub_category"].unique())

print("\n" + "=" * 60)
print("Unique Risk Categories")
print(df["risk_category"].unique())

print("\n" + "=" * 60)
print("AMFI Codes")
print(df["amfi_code"].head(10))