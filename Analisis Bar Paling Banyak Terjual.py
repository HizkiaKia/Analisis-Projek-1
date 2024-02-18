# Plot bar charts for top products by country
fig, ax = plt.subplots(figsize=(15, 10))
sns.barplot(x=top_products_by_country["Quantity"], y=top_products_by_country.index, hue=top_products_by_country["Top Product"], dodge=False, ax=ax)
ax.set_title("Top Products by Country")
ax.set_xlabel("Quantity")
ax.set_ylabel("Country")
plt.legend(loc="lower right")
plt.show()
