import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load dataset
# -----------------------------
dataset = pd.read_csv("Sales-Analysis.csv", encoding='latin1')

# -----------------------------
# Check missing values
# -----------------------------
print("Missing values:\n", dataset.isnull().sum())

# -----------------------------
# Convert dates
# -----------------------------
dataset['Order_Date'] = pd.to_datetime(dataset['Order_Date'], dayfirst=True)
dataset['Ship_Date'] = pd.to_datetime(dataset['Ship_Date'], dayfirst=True)

# -----------------------------
# Total Sales
# -----------------------------
total_sales = dataset['Sales'].sum()
print("Total Sales:", total_sales)

# -----------------------------
# Monthly Sales
# -----------------------------
monthly_sales = dataset.groupby(dataset['Order_Date'].dt.to_period('M'))['Sales'].sum()
# Convert PeriodIndex to datetime for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()
print("Monthly Sales:\n", monthly_sales)

# -----------------------------
# Average Order Value (AOV)
# -----------------------------
average_order_value = dataset.groupby('Order_ID')['Sales'].sum().mean()
print("Average Order Value:", average_order_value)

# -----------------------------
# Top 10 Products
# -----------------------------
top_products = dataset.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("Top 10 Products:\n", top_products)

# -----------------------------
# Best & Worst Regions
# -----------------------------
region_sales = dataset.groupby('Region')['Sales'].sum()
print("Best Region:", region_sales.idxmax())
print("Worst Region:", region_sales.idxmin())

# -----------------------------
# Monthly Sales Growth %
# -----------------------------
sales_growth = monthly_sales.pct_change() * 100
print("Monthly Sales Growth %:\n", sales_growth)

# -----------------------------
# Prepare month labels for charts
# -----------------------------
month_labels = monthly_sales.index.strftime('%b-%Y')  # Jan-2015, Feb-2015, etc.

# -----------------------------
# Plotting
# -----------------------------
sns.set_style("whitegrid")

# Monthly Sales Trend
plt.figure(figsize=(12,6))
sns.lineplot(x=month_labels, y=monthly_sales.values, marker='o', color='blue')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 Products by Sales
plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Products by Sales', fontsize=16)
plt.xlabel('Sales')
plt.ylabel('Product')
plt.tight_layout()
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette='magma')
plt.title('Sales by Region', fontsize=16)
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Monthly Sales Growth %
plt.figure(figsize=(12,6))
sns.barplot(x=month_labels, y=sales_growth.values, color='skyblue')
plt.title('Monthly Sales Growth %', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Growth %')
plt.xticks(rotation=45)
plt.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()
