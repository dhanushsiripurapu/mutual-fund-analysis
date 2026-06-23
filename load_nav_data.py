import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mutual_funds.db")

files = [
    "SBI_Bluechip.csv",
    "ICICI_Bluechip.csv",
    "Nippon_LargeCap.csv",
    "Axis_Bluechip.csv",
    "Kotak_Bluechip.csv",
    "hdfc_top100_nav.csv"
]

all_data = []

for file in files:

    df = pd.read_csv(f"data/raw/{file}")

    df["fund_name"] = file.replace(".csv", "")

    all_data.append(df)

nav_df = pd.concat(all_data)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print(nav_df.shape)
print("fact_nav table created")