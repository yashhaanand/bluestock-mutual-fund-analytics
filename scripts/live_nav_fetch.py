import os
import requests
import pandas as pd

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_PATH = os.path.join(BASE_DIR, "data", "api")

# Create api folder if it doesn't exist
os.makedirs(SAVE_PATH, exist_ok=True)

# ======================================================
# AMFI Scheme Codes
# ======================================================

SCHEMES = [
    119551,
    120503,
    118632,
    119092,
    120841
]

print("=" * 80)
print("Fetching Live NAV Data")
print("=" * 80)

successful_downloads = 0

for code in SCHEMES:

    url = f"https://api.mfapi.in/mf/{code}"

    try:

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        scheme_name = data["meta"]["scheme_name"]

        nav_df = pd.DataFrame(data["data"])

        # Make filename safe
        safe_name = (
            scheme_name
            .replace("/", "_")
            .replace("\\", "_")
            .replace("-", "_")
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
        )

        output_file = os.path.join(
            SAVE_PATH,
            f"{safe_name}.csv"
        )

        nav_df.to_csv(output_file, index=False)

        successful_downloads += 1

        print("\n" + "=" * 80)
        print(f"Scheme Code : {code}")
        print(f"Scheme Name : {scheme_name}")
        print(f"Records     : {len(nav_df)}")
        print(f"Date Range  : {nav_df['date'].min()} to {nav_df['date'].max()}")
        print(f"Saved As    : {os.path.basename(output_file)}")
        print("=" * 80)

    except requests.exceptions.Timeout:
        print(f"\n❌ Timeout while fetching Scheme Code: {code}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request Error for Scheme Code {code}: {e}")

    except Exception as e:
        print(f"\n❌ Unexpected Error for Scheme Code {code}: {e}")

print("\n" + "=" * 80)
print(f"Successfully downloaded {successful_downloads} out of {len(SCHEMES)} NAV datasets.")
print(f"Files saved in: {SAVE_PATH}")
print("=" * 80)