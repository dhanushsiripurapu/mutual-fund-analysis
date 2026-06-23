import requests
import pandas as pd

url = "https://api.mfapi.in/mf"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

df = pd.DataFrame(data)

print(df.head())

df.to_csv(
    "data/raw/01_fund_master.csv",
    index=False
)

print("Fund Master Saved")