import pandas as pd
import sqlite3

# Read cleaned data
df = pd.read_parquet("data/loan_clean.parquet")

# Create database
conn = sqlite3.connect("loan_risk.db")

# Load data into SQL table
df.to_sql(
    "loan_applications",
    conn,
    if_exists="replace",
    index=False
)

query = """
SELECT
Risk_Category,
COUNT(*) as total_customers
FROM loan_applications
GROUP BY Risk_Category
"""

result = pd.read_sql_query(
    query,
    conn
)

print(result)
df.to_csv(
    "dashboard/powerbi_dataset.csv",
    index=False
)