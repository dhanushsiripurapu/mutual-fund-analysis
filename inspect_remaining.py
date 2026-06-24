import pandas as pd

files = [
    "04_monthly_sip_inflows.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "="*60)
    print(file)

    df = pd.read_csv(f"data/raw/{file}")

    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())