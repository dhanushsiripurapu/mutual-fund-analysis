import pandas as pd
import sqlite3

conn = sqlite3.connect("mutual_funds.db")

# Load dim_fund
fund_df = pd.read_csv("data/raw/01_fund_master.csv")
fund_df.to_sql("dim_fund", conn, if_exists="replace", index=False)

# Load fact_nav
nav_df = pd.read_csv("data/raw/02_nav_history.csv")
nav_df.to_sql("fact_nav", conn, if_exists="replace", index=False)

# Load fact_aum
aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum_df.to_sql("fact_aum", conn, if_exists="replace", index=False)

conn.close()

print("Data Loaded Successfully")