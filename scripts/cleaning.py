import pandas as pd

df = pd.read_csv("data/train.csv.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing LoanAmount
df["LoanAmount"] = df["LoanAmount"].fillna(
    df["LoanAmount"].median()
)

# Fill missing Credit_History
df["Credit_History"] = df["Credit_History"].fillna(0)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

def risk_category(row):

    if row["Credit_History"] == 1:
        return "Low Risk"

    return "High Risk"

df["Risk_Category"] = df.apply(
    risk_category,
    axis=1
)

print(df["Risk_Category"].value_counts())

df.to_parquet(
    "data/loan_clean.parquet",
    index=False
)

print("Parquet file created successfully.")