import pandas as pd

df=pd.read_csv("data/train.csv.csv")
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())

quality_report = pd.DataFrame({
    "column_name": df.columns,
    "missing_count": df.isnull().sum().values
})

quality_report.to_csv(
    "reports/quality_report.csv",
    index=False
)

print("\nQuality report generated successfully.")