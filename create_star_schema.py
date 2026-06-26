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

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_sip(
    month TEXT,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL,
    new_sip_accounts_lakh REAL,
    sip_aum_lakh_crore REAL,
    yoy_growth_pct REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_category_inflows(
    month TEXT,
    category TEXT,
    net_inflow_crore REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_folio_count(
    month TEXT,
    folio_count_crore REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_scheme_performance(
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    sharpe_ratio REAL
)
""")


conn.commit()
conn.close()

print("Star Schema Created Successfully")