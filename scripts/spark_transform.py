
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "train.csv.csv"
OUTPUT_DIR = Path("C:/spark-output/loan-risk-curated")

spark = (
    SparkSession.builder
    .appName("LoanRiskSparkTransformation")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    print("Reading raw loan data...", flush=True)

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(INPUT_FILE))
    )

    print(f"Raw rows: {df.count()}", flush=True)
    print(f"Columns: {df.columns}", flush=True)

    # Remove duplicate records
    df = df.dropDuplicates()

    # Fill missing LoanAmount values with the median
    if "LoanAmount" in df.columns:
        median_values = df.approxQuantile(
            "LoanAmount", [0.5], 0.01
        )
        if median_values:
            df = df.fillna(
                {"LoanAmount": median_values[0]}
            )

    # Fill missing credit history
    if "Credit_History" in df.columns:
        df = df.fillna({"Credit_History": 0})

        # Create a rule-based risk category
        df = df.withColumn(
            "Risk_Category",
            F.when(
                F.col("Credit_History") == 1,
                F.lit("Low Risk")
            ).otherwise(F.lit("High Risk"))
        )

    print(f"Curated rows: {df.count()}", flush=True)
    df.groupBy("Risk_Category").count().show()

    # Save to a separate Parquet output directory
    df.write.mode("overwrite").parquet(str(OUTPUT_DIR))

    print(f"SUCCESS: Parquet saved to {OUTPUT_DIR}", flush=True)

finally:
    spark.stop()
