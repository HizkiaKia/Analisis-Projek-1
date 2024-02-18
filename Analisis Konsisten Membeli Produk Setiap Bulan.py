# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("https://www.kaggle.com/datasets/siddharththakkar26/online-retail-dataset")

# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract month and year from InvoiceDate
df["Month"] = df["InvoiceDate"].dt.month
df["Year"] = df["InvoiceDate"].dt.year

# Group by customer and month and year and aggregate by count
transactions_by_customer = df.groupby(["CustomerID", "Month", "Year"]).agg({"InvoiceNo": "nunique"})

# Reset index
transactions_by_customer = transactions_by_customer.reset_index()

# Pivot the table to get the number of transactions for each customer and each month and year
transactions_by_customer = transactions_by_customer.pivot_table(index="CustomerID", columns=["Month", "Year"], values="InvoiceNo", fill_value=0)

# Create a new column to indicate whether the customer has transactions every month
transactions_by_customer["Consistent"] = transactions_by_customer.apply(lambda x: x.min() > 0, axis=1)

# Display the table
transactions_by_customer
