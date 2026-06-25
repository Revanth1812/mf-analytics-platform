import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = fund_codes - nav_codes

print("=" * 60)
print(f"Fund Master AMFI Codes : {len(fund_codes)}")
print(f"NAV History AMFI Codes : {len(nav_codes)}")

print("\n" + "=" * 60)

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master are available in nav_history.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print("\n" + "=" * 60)
print("Data Quality Summary")
print("- No duplicate AMFI codes checked in this script.")
print("- AMFI code consistency validated between datasets.")