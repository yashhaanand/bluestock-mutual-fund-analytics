import os
import pandas as pd

# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw")

# ==============================
# Get all CSV files
# ==============================

csv_files = sorted(
    [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]
)

print("=" * 80)
print(f"Found {len(csv_files)} CSV files")
print("=" * 80)

# ==============================
# Read and Analyze each dataset
# ==============================

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"Processing Dataset : {file}")
    print("=" * 80)

    file_path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(file_path)

    print(f"Shape            : {df.shape}")
    print(f"Columns          : {len(df.columns)}")
    print(f"Duplicate Rows   : {df.duplicated().sum()}")
    print(f"Missing Values   : {df.isnull().sum().sum()}")

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

print("\n" + "=" * 80)
print("All datasets loaded successfully.")
print("=" * 80)