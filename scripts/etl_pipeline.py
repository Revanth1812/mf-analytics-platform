import subprocess
import sys

scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_scheme_performance.py",
    "clean_investor_transactions.py",
    "load_to_sqlite.py"
]

print("Starting ETL Pipeline...\n")

for script in scripts:
    print(f"Running {script}...")
    subprocess.run([sys.executable, script], check=True)

print("\nETL Pipeline Completed Successfully.")