import sqlite3
import pandas as pd

conn = sqlite3.connect("mutual_funds.db")

tables = ["dim_fund", "fact_nav", "fact_aum"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    print(f"\n{table}")
    print("Rows:", len(df))
    print(df.head())

conn.close()