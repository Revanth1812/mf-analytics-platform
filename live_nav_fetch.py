import requests
import pandas as pd
from pathlib import Path

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}


output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)


for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = output_folder / f"{scheme_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"✅ {scheme_name} downloaded successfully.")

    else:
        print(f"❌ Failed to fetch {scheme_name}")