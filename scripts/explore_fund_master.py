import os
import pandas as pd

# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")

df = pd.read_csv(FILE_PATH)

print("=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

print(f"\nTotal Fund Houses : {df['fund_house'].nunique()}")
print(df["fund_house"].unique())

print(f"\nTotal Categories : {df['category'].nunique()}")
print(df["category"].unique())

print(f"\nTotal Sub Categories : {df['sub_category'].nunique()}")
print(df["sub_category"].unique())

print(f"\nTotal Risk Categories : {df['risk_category'].nunique()}")
print(df["risk_category"].unique())