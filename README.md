# 📊 Robust Transaction Data Cleaning & Feature Engineering Pipeline

A production-grade, modular Python pipeline built with **Pandas** and **NumPy** to clean, standardize, and audit messy transactional sales data. 

## 🎯 Project Overview
This project transforms a highly chaotic raw dataset into an analytical-ready DataFrame. It replaces basic script execution with a **modular function-based architecture** featuring structural validations, comprehensive logging, and defensive programming to ensure enterprise reliability.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy
* **Core Modules:** Logging

## 🚀 Key Features & Pipeline Architecture

### 1. Production-Grade Reliability
* **Functional Architecture:** Core logic is encapsulated inside `clean_transaction_data()` for seamless integration into larger ETL workflows.
* **Defensive Schema Validation:** Explicit checks for mandatory columns throw a structural `KeyError` before execution to prevent silent down-stream script failures.
* **Unified Error Logging:** Replaces generic print statements with structured `logging` levels (`INFO`, `WARNING`, `ERROR`) tracking execution steps and timestamps.
* **Division-by-Zero Protection:** Uses vector-based `np.where` conditionally to safely calculate profit margins without encountering mathematical infinity errors.

### 2. Advanced Data Imputation & Engineering
* **Outlier Mitigation:** Removes extreme absolute data anomalies and applies the statistical **Interquartile Range (IQR)** method to handle distribution skewness.
* **Smart Imputation:** Dynamically replaces missing numbers with conditional central tendencies (**Median** for Sales, **Mean** for Profit).
* **Multi-Conditional Risk Auditing:** Runs an advanced matrix using `np.select` to auto-categorize sales tiers and flag transactional compliance risks (`Performance_Risk_Audit`).

## ⚙️ How To Run

1. Clone this repository:
```bash
git clone <your-repository-link>
```

2. Activate your virtual environment and run the script:
```bash
python dirty_sales_dataset.py
```

## 📊 Sample Output Schema
The final engineered dataset produces the following clean structured fields:


| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Transaction_ID** | Object / Str | Unique transactional identification key (Deduplicated) |
| **Product_Name** | Object / Str | Standardized upper-case alphanumeric values |
| **Region** | Object / Str | Trimmed and normalized title-case regional sectors |
| **Sales_Amount** | Float64 | Sanitized and imputed transaction values |
| **Profit_Earned** | Float64 | Cleaned positive margin values (Imputed via Mean) |
| **Profit_Margin_%** | Float64 | Calculated financial margin indicator |
| **Sales_Category** | Categorical | Revenue scales segmented into low, medium, or high |
| **Performance_Risk_Audit** | Object / Str | Rule-based performance metric profiling |
