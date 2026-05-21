# 📊 Transaction Data Cleaning & Feature Engineering Pipeline

A Python-based data engineering pipeline built with **Pandas** and **NumPy** to clean, standardize, and audit messy transactional sales data. 

## 🎯 Project Overview
Raw business data is often filled with inconsistencies like duplicate transactions, mixed casing, currency formatting issues, unrealistic outliers, and missing values. This project automates the transition from a highly chaotic dataset into an analytical-ready DataFrame, followed by statistical segmentation and risk profiling.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy

## 🚀 Key Features & Pipeline Steps

### 1. Data Deduplication & Standardization
* **Unique Constraints:** Removes duplicate rows based on `Transaction_ID` while keeping the first occurrence.
* **Text Formatting:** Standardizes `Product_Name` to upper case and `Region` to title case.
* **Inconsistency Resolution:** Handles whitespace trimming and maps inconsistent labels (e.g., `None` or missing values are categorized as `Unknown`).

### 2. Robust Currency & Numerical Parsing
* **Regex Cleaning:** Strips currency symbols (`$`) and commas from monetary columns.
* **Type Conversion:** Force-casts variables into numerical float types (`pd.to_numeric`).

### 3. Outlier Mitigation & Filtering
* **Domain Constraint Removal:** Flags and voids extreme artificial data points (e.g., values $> \$50,000$).
* **Logical Correction:** Sets negative profits to `NaN` as profit cannot realistically be negative under these system rules.
* **Statistical Filtering:** Uses the **Interquartile Range (IQR)** method to detect and remove distribution outliers beyond the upper boundary ($Q3 + 1.5 \times IQR$).

### 4. Smart Imputation Strategy
* **Sales Amount:** Replaces missing data and treated outliers with the **Median** to avoid skewness.
* **Profit Earned:** Replaces missing figures with the **Mean** value.
* **Categorical Data:** Imputes missing return policy entries as `'Unknown'`.

### 5. Advanced Feature Engineering
* **Profit Margin:** Calculates `Profit_Margin_%` dynamically.
* **Sales Binning:** Groups revenue scales into categorical segments (`Low_Sales`, `Medium_Sales`, `High_Sales`) using `pd.cut`.
* **Performance Risk Audit:** Executes a multi-conditional rule matrix (`np.select`) to assign risk tiers:
  * `Highly_Profitable_Safe`
  * `Standard_Risk`
  * `Low_Margin_Or_High_Return_Risk`
  * `Review_Required`

## ⚙️ How To Run

1. Clone this repository:
```bash
git clone <your-repository-link>
```

2. Install dependencies:
```bash
pip install pandas numpy
```

3. Run the script:
```bash
python data_cleaning.py
```

## 📊 Sample Output Format
The resulting output provides a structured schema optimized for downstream BI tools or machine learning models:


| Transaction_ID | Product_Name | Region | Sales_Amount | Profit_Earned | Return_Policy_Met | Profit_Margin_% | Sales_Category | Performance_Risk_Audit |
|----------------|--------------|--------|--------------|---------------|-------------------|-----------------|----------------|------------------------|
| TXN-1000       | PRODUCT_A    | North  | 450.00       | 95.50         | Yes               | 21.22           | Medium_Sales   | Standard_Risk          |
