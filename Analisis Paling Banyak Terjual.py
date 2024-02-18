# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("https://www.kaggle.com/datasets/siddharththakkar26/online-retail-dataset")

# Group by country and product and aggregate by sum
products_by_country = df.groupby(["Country", "Description"]).agg({"Quantity": "sum"})

# Sort by quantity in descending order
products_by_country = products_by_country.sort_values(by="Quantity", ascending=False)

# Reset index
products_by_country = products_by_country.reset_index()

# Get the top product for each country
top_products_by_country = products_by_country.groupby("Country").first()

# Rename columns
top_products_by_country.columns = ["Top Product", "Quantity"]

# Display the table
top_products_by_country
