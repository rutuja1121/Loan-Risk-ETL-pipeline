# Loan Risk ETL Pipeline

## Overview

This project demonstrates the design and implementation of an end-to-end Loan Risk ETL Pipeline for processing, validating, and analyzing loan application data. The pipeline automates data quality checks, data cleaning, risk classification, analytical reporting, and dashboard generation.

The project simulates a real-world banking and fintech use case where loan application data is processed and transformed into actionable business insights.

---

## Architecture

Raw CSV Data
↓
Python ETL Pipeline
↓
Data Quality Validation
↓
Data Cleaning & Transformation
↓
Risk Classification
↓
Parquet Storage
↓
SQL Analytics Layer (SQLite)
↓
Power BI Dashboard

---

## Business Problem

Financial institutions process thousands of loan applications daily. Poor data quality and inconsistent records can impact risk assessment and lending decisions.

This project addresses these challenges by:

* Validating incoming loan application data
* Handling missing and inconsistent records
* Classifying customer risk profiles
* Generating analytical datasets
* Enabling business reporting through Power BI

---

## Tech Stack

### Programming & Data Processing

* Python
* Pandas
* NumPy

### Data Storage

* CSV
* Parquet
* SQLite

### Analytics & Visualization

* SQL
* Power BI

### Version Control

* Git
* GitHub

---

## Project Structure

Loan-Risk-ETL-Pipeline

├── data
│   ├── train.csv
│   └── loan_clean.parquet
│
├── scripts
│   ├── cleaning.py
│   └── sql_analysis.py
│
├── reports
│   └── quality_report.csv
│
├── dashboard
│   ├── powerbi_dataset.csv
│   └── Loan_Risk_Dashboard.pbix
│
├── screenshots
│   └── dashboard.png
│
├── README.md
│
└── loan_risk.db

---

## ETL Workflow

### 1. Extract

* Load raw loan application data from CSV files
* Validate schema and column structure

### 2. Transform

* Remove duplicate records
* Handle missing values
* Standardize data formats
* Create Risk_Category field

### 3. Load

* Store processed data in Parquet format
* Load analytical dataset into SQLite database
* Export reporting dataset for Power BI

---

## Data Quality Checks

The pipeline performs automated validation including:

* Missing value analysis
* Duplicate record detection
* Data consistency checks
* Quality report generation

Generated reports are stored in the reports folder.

---

## Risk Classification Logic

Applicants are categorized into:

### Low Risk

* Credit_History = 1

### High Risk

* Credit_History = 0

This logic can be extended using additional business rules and predictive models.

---

## Dashboard Features

The Power BI dashboard provides:

### KPI Metrics

* Total Applications
* Average Loan Amount
* Average Applicant Income

### Risk Analytics

* Risk Distribution
* Applications by Risk Category

### Geographic Analysis

* Average Loan Amount by Property Area

### Operational Monitoring

* High Risk Customer Listing
* Interactive Filtering

---

## Sample Dashboard

Add a screenshot of your dashboard below:

![Loan Risk Dashboard](screenshots/dashboard.png)

---

## Key Outcomes

* Automated ETL processing workflow
* Improved data quality and consistency
* Business-ready analytical dataset
* Interactive reporting dashboard
* End-to-end data engineering project implementation

---

## Future Enhancements

* AWS S3 Integration
* PySpark Processing
* AWS Glue ETL Jobs
* Redshift Data Warehouse
* Machine Learning Risk Scoring
* Automated Scheduling with Apache Airflow

---

## Author

Rutuja Patil

Aspiring Data Engineer | Python | SQL | Cloud Data Engineering | Analytics
