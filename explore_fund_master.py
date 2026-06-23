import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Rows, Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())
print(df.shape)