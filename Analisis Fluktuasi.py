# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("https://www.kaggle.com/datasets/siddharththakkar26/online-retail-dataset")

# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract hour from InvoiceDate
df["Hour"] = df["InvoiceDate"].dt.hour

# Filter out weekends
df = df[df["InvoiceDate"].dt.dayofweek < 5]

# Group by hour and aggregate by count and sum
sales_by_hour = df.groupby("Hour").agg({"InvoiceNo": "nunique", "Quantity": "sum", "Total": "sum"})

# Rename columns
sales_by_hour.columns = ["Transactions", "Products", "Sales"]

# Plot line charts for transactions, products, and sales by hour
fig, ax = plt.subplots(3, 1, figsize=(12, 15))
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour["Transactions"], ax=ax[0])
ax[0].set_title("Transactions by Hour")
ax[0].set_xlabel("Hour")
ax[0].set_ylabel("Transactions")
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour["Products"], ax=ax[1])
ax[1].set_title("Products by Hour")
ax[1].set_xlabel("Hour")
ax[1].set_ylabel("Products")
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour["Sales"], ax=ax[2])
ax[2].set_title("Sales by Hour")
ax[2].set_xlabel("Hour")
ax[2].set_ylabel("Sales")
plt.tight_layout()
plt.show()
