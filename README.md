# 📊 Robust Transaction Data Cleaning, Analytics & Visualization Pipeline

A production-grade, modular Python pipeline built with **Pandas**, **NumPy**, and **Seaborn** to clean, analyze, and visually map messy transactional sales data.

## 🎯 Project Overview
This project transforms a highly chaotic raw dataset into an analytical-ready DataFrame. Moving beyond basic data cleaning, the pipeline now executes automated business aggregations and generates advanced statistical visualizations (such as bivariate scatter arrays and Kernel Density Estimates) to discover hidden performance trends and compliance risks.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Core Modules:** Logging

## 🚀 Key Features & Pipeline Architecture

### 1. Production-Grade Reliability & Validation
* **Functional ETL Design:** Logic is encapsulated inside production-ready modules for clean debugging and seamless orchestration.
* **Defensive Schema Checks:** Verifies structural requirements upfront and raises descriptive system errors if critical data fields are missing.
* **Unified Logging Framework:** Leverages Python’s native logging matrix to track step-by-step processing intervals and operation timestamps.
* **Mathematical Vectorization:** Prevents zero-division errors during profit execution using targeted NumPy vector tracking.

### 2. Analytical Transformation & Imputation
* **Statistical Outlier Filtration:** Eradicates artificial monetary spikes and maps data variances using the **Interquartile Range (IQR)** formula.
* **Conditional Distribution Imputation:** Replaces missing figures or dropped values safely using the sample **Median** for sales and **Mean** for profits.
* **Algorithmic Audit Matrix:** Runs multi-conditional rule parsing via `np.select` to capture operational hazards and safety metrics (`Performance_Risk_Audit`).

### 3. Business Intelligence & Advanced Plots
* **Product Performance Analytics:** Aggregates overall unit volume, total revenue streams, and localized margins across item variants.
* **Multi-Distribution Density Mapping:** Generates automated **Kernel Density Estimate (KDE) Plots** to contrast profit percentages across split revenue tiers.
* **Bivariate Multi-Plot Scatter Matrix:** Plots correlation grids across dimensional variables using deep categorical palettes (`viridis`, `magma`).

## ⚙️ How To Run

1. Clone this repository:
```bash
git clone <your-repository-link>
```

2. Activate your virtual environment and install dependencies:
```bash
pip install pandas numpy matplotlib seaborn
```

3. Run the complete pipeline script:
```bash
python dirty_sales_dataset.py
```

## 📊 Sample Output Schema


| Column Name | Data Type | Analytical Context |
| :--- | :--- | :--- |
| **Transaction_ID** | Object / Str | Deduplicated system keys mapping specific unique items |
| **Product_Name** | Object / Str | Cleaned upper-case clean text tracking inventory metrics |
| **Region** | Object / Str | Normalized regional business blocks |
| **Sales_Amount** | Float64 | Sanitized and imputed revenue totals |
| **Profit_Earned** | Float64 | Logical positive metrics imputed via mean distributions |
| **Profit_Margin_%** | Float64 | Calculated revenue-to-margin percentages |
| **Sales_Category** | Categorical | Revenue segments categorized into Low, Medium, or High tiers |
| **Performance_Risk_Audit**| Object / Str | Compliance and profit categorization profiling groups |
