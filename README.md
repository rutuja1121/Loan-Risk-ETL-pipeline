
# Loan Risk Analytics Pipeline

## Overview
An end-to-end data analytics project that processes
loan application data, performs data cleaning and
risk categorization, stores analytical data in SQLite,
and prepares datasets for Power BI reporting.

## Tech Stack
- Python
- Pandas
- SQL
- SQLite
- Parquet
- Power BI

## Project Workflow
1. Profile the raw loan application dataset.
2. Generate a data quality report.
3. Clean and transform the data.
4. Store and analyze the processed data using SQLite.
5. Export data for Power BI visualization.

## Project Structure
- data/       - Input and processed datasets
- scripts/    - ETL, cleaning and SQL scripts
- reports/    - Data quality reports
- dashboard/  - Dashboard and reporting files

## How to Run
Run the following commands from the project root:

    python scripts/etl.py
    python scripts/cleaning.py
    python scripts/sql_analysis.py

If run_pipeline.py has been created and tested:

    python run_pipeline.py

## Dashboard
The Power BI dashboard presents loan application
counts, risk categories, loan status and loan
amount comparisons, depending on the available fields.

## Limitations
Risk categories are based on the implemented rules.
They should not be interpreted as a validated
credit-risk prediction model.
