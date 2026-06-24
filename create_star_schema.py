import sqlite3

conn = sqlite3.connect("mutual_funds.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_nav(
    amfi_code INTEGER,
    date TEXT,
    nav REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_aum(
    date TEXT,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER
)
""")

conn.commit()
conn.close()

print("Star Schema Created Successfully")