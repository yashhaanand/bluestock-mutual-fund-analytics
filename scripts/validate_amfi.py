import os
import pandas as pd

# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

master = pd.read_csv(
    os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")
)

nav = pd.read_csv(
    os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv")
)

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing_codes = master_codes - nav_codes

print("=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes from fund_master exist in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    for code in sorted(missing_codes):
        print(code)

print("=" * 80)