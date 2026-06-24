import pandas as pd
import sqlite3

conn = sqlite3.connect("mutual_funds.db")

pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
).to_sql(
    "fact_sip",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/08_investor_transactions.csv"
).to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
).to_sql(
    "fact_holdings",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
).to_sql(
    "fact_benchmark",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Remaining tables loaded successfully")