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
pd.read_csv(
    "data/raw/05_category_inflows.csv"
).to_sql(
    "fact_category_inflows",
    conn,
    if_exists="replace",
    index=False
)
pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
).to_sql(
    "fact_folio_count",
    conn,
    if_exists="replace",
    index=False
)
pd.read_csv(
    "data/raw/07_scheme_performance.csv"
).to_sql(
    "fact_scheme_performance",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Remaining tables loaded successfully")