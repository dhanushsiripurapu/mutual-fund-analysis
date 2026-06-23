import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mutual_funds.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully")