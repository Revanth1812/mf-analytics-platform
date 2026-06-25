import pandas as pd
from pathlib import Path

# Raw data folder
raw_path = Path("data/raw")

# Get all CSV files
csv_files = raw_path.glob("*.csv")

# Read and display basic information
for file in csv_files:
    print("=" * 60)
    print(f"File Name : {file.name}")

    df = pd.read_csv(file)

    print(f"\nShape:\n{df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("=" * 60)