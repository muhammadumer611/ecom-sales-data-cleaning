import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Logging Setup
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_messy_data(n_rows=500) -> pd.DataFrame:
    """Generates the initial messy dataset for testing."""
    np.random.seed(42)

    products = [
        "Product_A",
        "Product_B",
        "Product_C",
        "Product_D",
        "Product_E",
        "Product_F",
        "prod_a",
        "PRODUCT_B",
        "  Product_C  ",
    ]
    regions = [
        "North",
        "South",
        "East",
        "West",
        "Northeast",
        "south",
        "Unknown",
        None,
    ]

    df_messy = pd.DataFrame(
        {
            "Transaction_ID": [f"TXN-{1000 + i}" for i in range(n_rows)],
            "Product_Name": np.random.choice(products, n_rows),
            "Region": np.random.choice(regions, n_rows),
            "Sales_Amount": [
                f"${val:,.2f}" if np.random.rand() > 0.05 else np.nan
                for val in np.random.randint(50, 1500, n_rows).astype(float)
            ],
            "Profit_Earned": np.random.randint(50, 1500, n_rows)
            * np.random.uniform(0.1, 0.35, n_rows),
            "Return_Policy_Met": np.random.choice(
                ["Yes", "No", "Y", "N", None], n_rows
            ),
        }
    )

    df_messy.loc[
        np.random.choice(n_rows, 30, replace=False), "Profit_Earned"
    ] = np.nan
    df_messy = pd.concat([df_messy, df_messy.iloc[10:25]], ignore_index=True)
    df_messy.loc[5, "Sales_Amount"] = "$999,999.00"
    df_messy.loc[12, "Profit_Earned"] = -5000.0

    return df_messy


def clean_transaction_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Takes a messy transactional DataFrame, cleans it, handles outliers,

    and returns a structured, engineered DataFrame.
    """
    if df_raw.empty:
        logging.warning("Input DataFrame is empty!")
        return df_raw

    df = df_raw.copy()

    required_cols = [
        "Transaction_ID",
        "Product_Name",
        "Region",
        "Sales_Amount",
        "Profit_Earned",
        "Return_Policy_Met",
    ]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing mandatory columns in input data: {missing_cols}")

    try:
        # --- Step 1: Deduplication & Text Cleaning ---
        logging.info("Starting text cleaning and deduplication...")
        df = df.drop_duplicates(subset=["Transaction_ID"], keep="first")

        df["Product_Name"] = (
            df["Product_Name"].astype(str).str.strip().str.upper()
        )
        df["Region"] = (
            df["Region"]
            .astype(str)
            .str.strip()
            .str.title()
            .replace({"None": "Unknown", "Nan": "Unknown"})
        )

        # --- Step 2: Currency & Numeric Conversion ---
        logging.info("Parsing currency values...")
        if df["Sales_Amount"].dtype == object:
            df["Sales_Amount"] = df["Sales_Amount"].str.replace(
                r"[\$,]", "", regex=True
            )
        df["Sales_Amount"] = pd.to_numeric(df["Sales_Amount"], errors="coerce")
        df["Profit_Earned"] = pd.to_numeric(
            df["Profit_Earned"], errors="coerce"
        )

        # --- Step 3: Outlier & Anomaly Detection ---
        logging.info("Handling anomalies and IQR statistical outliers...")
        df.loc[df["Sales_Amount"] > 50000, "Sales_Amount"] = np.nan
        df.loc[df["Profit_Earned"] < 0, "Profit_Earned"] = np.nan

        q1 = df["Sales_Amount"].quantile(0.25)
        q3 = df["Sales_Amount"].quantile(0.75)
        if not pd.isna(q1) and not pd.isna(q3):
            iqr = q3 - q1
            upper_bound = q3 + (1.5 * iqr)
            df.loc[df["Sales_Amount"] > upper_bound, "Sales_Amount"] = np.nan

        # --- Step 4: Smart Imputation ---
        logging.info("Imputing missing values...")
        sales_median = df["Sales_Amount"].median()
        profit_mean = df["Profit_Earned"].mean()

        df["Sales_Amount"] = df["Sales_Amount"].fillna(
            sales_median if pd.notna(sales_median) else 0.0
        )
        df["Profit_Earned"] = df["Profit_Earned"].fillna(
            profit_mean if pd.notna(profit_mean) else 0.0
        )

        df["Return_Policy_Met"] = (
            df["Return_Policy_Met"]
            .replace({"Y": "Yes", "N": "No"})
            .fillna("Unknown")
        )

        # --- Step 5: Feature Engineering & Risk Audit ---
        logging.info("Performing feature engineering and risk auditing...")
        df["Profit_Margin_%"] = np.where(
            df["Sales_Amount"] != 0,
            np.round((df["Profit_Earned"] / df["Sales_Amount"]) * 100, 2),
            0.0,
        )

        sales_bins = [0, 400, 1000, np.inf]
        sales_labels = ["Low_Sales", "Medium_Sales", "High_Sales"]
        df["Sales_Category"] = pd.cut(
            df["Sales_Amount"],
            bins=sales_bins,
            labels=sales_labels,
            include_lowest=True,
        )

        conditions = [
            (df["Profit_Margin_%"] > 25) & (df["Return_Policy_Met"] == "No"),
            (df["Profit_Margin_%"] <= 25) & (df["Profit_Margin_%"] >= 10),
            (df["Profit_Margin_%"] < 10) | (df["Return_Policy_Met"] == "Yes"),
        ]
        choices = [
            "Highly_Profitable_Safe",
            "Standard_Risk",
            "Low_Margin_Or_High_Return_Risk",
        ]
        df["Performance_Risk_Audit"] = np.select(
            conditions, choices, default="Review_Required"
        )

        logging.info("Data pipeline executed successfully!")
        return df

    except Exception as e:
        logging.error(f"Pipeline failed during execution: {str(e)}")
        raise


def run_business_analytics(df: pd.DataFrame):
    """Performs deep aggregations and prints core insights."""
    print("\n" + "=" * 45)
    print("📈 SECTION 1: BUSINESS INSIGHTS & AGGREGATIONS")
    print("=" * 45)

    # 1. Product Matrix
    print("\n[📊] Product Performance Metrics:")
    product_matrix = (
        df.groupby("Product_Name")
        .agg(
            Total_Revenue=("Sales_Amount", "sum"),
            Avg_Profit_Margin=("Profit_Margin_%", "mean"),
            Volume=("Transaction_ID", "count"),
        )
        .sort_values(by="Total_Revenue", ascending=False)
    )
    print(product_matrix.round(2))

    # 2. Risk Distribution
    print("\n[⚠️] Audit Compliance & Risk Value Counts:")
    risk_matrix = df["Performance_Risk_Audit"].value_counts()
    print(risk_matrix)


def plot_statistical_distributions(df: pd.DataFrame):
    """Generates advanced statistical charts using Seaborn."""
    logging.info("Generating data distribution charts...")

    # Theme config
    sns.set_theme(style="darkgrid")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Chart 1: Multi-Density KDE Plot (Profit Margin vs Sales Categories)
    sns.kdeplot(
        data=df,
        x="Profit_Margin_%",
        hue="Sales_Category",
        fill=True,
        common_norm=False,
        palette="viridis",
        alpha=0.4,
        linewidth=2,
        ax=axes[0],
    )
    axes[0].set_title(
        "Kernel Density Estimate (KDE) of Profit Margin",
        fontsize=13,
        weight="bold",
    )
    axes[0].set_xlabel("Profit Margin (%)")
    axes[0].set_ylabel("Probability Density")

    # Chart 2: Bivariate Distribution (Sales Amount vs Profit Earned with Hue)
    sns.scatterplot(
        data=df,
        x="Sales_Amount",
        y="Profit_Earned",
        hue="Performance_Risk_Audit",
        palette="magma",
        alpha=0.7,
        ax=axes[1],
    )
    axes[1].set_title(
        "Bivariate Clustering: Sales vs Profit Dynamics",
        fontsize=13,
        weight="bold",
    )
    axes[1].set_xlabel("Sales Amount ($)")
    axes[1].set_ylabel("Profit Earned ($)")

    plt.tight_layout()
    logging.info("Displaying charts. Close the window to finalize script.")
    plt.show()


# --- Execution ---
if __name__ == "__main__":
    try:
        # Step 1: Data creation
        df_messy = generate_messy_data(n_rows=500)

        # Step 2: Running engineering pipeline
        df_cleaned = clean_transaction_data(df_messy)

        # Step 3: Extract business metrics
        run_business_analytics(df_cleaned)

        # Step 4: Trigger Seaborn graphs
        plot_statistical_distributions(df_cleaned)

    except Exception as pipeline_error:
        print(f"Main Execution Stopped: {pipeline_error}")
