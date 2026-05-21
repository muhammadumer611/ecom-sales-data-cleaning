import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 500

products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E', 'Product_F', 'prod_a', 'PRODUCT_B', '  Product_C  ']
regions = ['North', 'South', 'East', 'West', 'Northeast', 'south', 'Unknown', None]

df_messy = pd.DataFrame({
    'Transaction_ID': [f"TXN-{1000 + i}" for i in range(n_rows)],
    'Product_Name': np.random.choice(products, n_rows),
    'Region': np.random.choice(regions, n_rows),
    'Sales_Amount': [f"${val:,.2f}" if np.random.rand() > 0.05 else np.nan for val in np.random.randint(50, 1500, n_rows).astype(float)],
    'Profit_Earned': np.random.randint(50, 1500, n_rows) * np.random.uniform(0.1, 0.35, n_rows),
    'Return_Policy_Met': np.random.choice(['Yes', 'No', 'Y', 'N', None], n_rows)
})

df_messy.loc[np.random.choice(n_rows, 30, replace=False), 'Profit_Earned'] = np.nan
df_messy = pd.concat([df_messy, df_messy.iloc[10:25]], ignore_index=True)
df_messy.loc[5, 'Sales_Amount'] = "$999,999.00"
df_messy.loc[12, 'Profit_Earned'] = -5000.0

df_cleaned_data = df_messy.drop_duplicates(subset=['Transaction_ID'], keep='first').copy()

df_cleaned_data['Product_Name'] = df_cleaned_data['Product_Name'].str.strip().str.upper()
df_cleaned_data['Region'] = df_cleaned_data['Region'].str.strip().str.title().replace({'None': 'Unknown', 'Unknown': 'Unknown'})

df_cleaned_data['Sales_Amount'] = df_cleaned_data['Sales_Amount'].str.replace('[\$,]', '', regex=True)
df_cleaned_data['Sales_Amount'] = pd.to_numeric(df_cleaned_data['Sales_Amount'], errors='coerce')

df_cleaned_data.loc[df_cleaned_data['Sales_Amount'] > 50000, 'Sales_Amount'] = np.nan
df_cleaned_data.loc[df_cleaned_data['Profit_Earned'] < 0, 'Profit_Earned'] = np.nan

q1, q3 = df_cleaned_data['Sales_Amount'].quantile([0.25, 0.75])
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)
df_cleaned_data.loc[df_cleaned_data['Sales_Amount'] > upper_bound, 'Sales_Amount'] = np.nan

df_cleaned_data['Sales_Amount'] = df_cleaned_data['Sales_Amount'].fillna(df_cleaned_data['Sales_Amount'].median())
df_cleaned_data['Profit_Earned'] = df_cleaned_data['Profit_Earned'].fillna(df_cleaned_data['Profit_Earned'].mean())

df_cleaned_data['Return_Policy_Met'] = df_cleaned_data['Return_Policy_Met'].replace({'Y': 'Yes', 'N': 'No'}).fillna('Unknown')

df_cleaned_data['Profit_Margin_%'] = np.round((df_cleaned_data['Profit_Earned'] / df_cleaned_data['Sales_Amount']) * 100, 2)

sales_bins = [0, 400, 1000, np.inf]
sales_labels = ['Low_Sales', 'Medium_Sales', 'High_Sales']
df_cleaned_data['Sales_Category'] = pd.cut(df_cleaned_data['Sales_Amount'], bins=sales_bins, labels=sales_labels)

conditions = [
    (df_cleaned_data['Profit_Margin_%'] > 25) & (df_cleaned_data['Return_Policy_Met'] == 'No'),
    (df_cleaned_data['Profit_Margin_%'] <= 25) & (df_cleaned_data['Profit_Margin_%'] >= 10),
    (df_cleaned_data['Profit_Margin_%'] < 10) | (df_cleaned_data['Return_Policy_Met'] == 'Yes')
]
choices = ['Highly_Profitable_Safe', 'Standard_Risk', 'Low_Margin_Or_High_Return_Risk']
df_cleaned_data['Performance_Risk_Audit'] = np.select(conditions, choices, default='Review_Required')

print(df_cleaned_data.head(200))
