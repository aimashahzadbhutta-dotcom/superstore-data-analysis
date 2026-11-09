from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fig, axes = plt.subplots(1,3, figsize=(15,4))
fig.suptitle("Sales Dashboard", fontsize=16, fontweight='bold')

plt.style.use("ggplot")
df = pd.read_csv("train.csv")
sales = df["Sales"]
array = np.array(sales)
bins = np.arange(0, 5000, 11)
median = np.median(array)
axes[0].hist(array, bins=bins, width=6, label="Sales", log=True)
color='#fc4f30'
axes[0].axvline(median, color=color, label='Sales Median')
axes[0].set_xlabel("Sales")
axes[0].set_ylabel("Frequency of Sale values")
axes[0].legend()
max = array.max()
axes[0].set_title(f"Sales Distribution(zoomed 0 to 5,000; full maximum: {max})", fontsize=10)

region = df["Region"]
array1 = np.array(region)
axes[1].bar(array1, array, color='C3', width=0.3, label="Total Sales per Region")
axes[1].legend()
axes[1].set_xlabel("Region")
axes[1].set_ylabel("Sales")
axes[1].set_title("Region vs Sales", fontsize=10)

df["Order Date"] = pd.to_datetime(df["Order Date"])
date = df["Order Date"]
sc = axes[2].scatter(date, array, c=array, cmap='viridis', edgecolor='black', linewidth=1)
cbar = fig.colorbar(sc, ax=axes[2])
cbar.set_label("Sales")
axes[2].set_xlabel("Order Date")
axes[2].set_ylabel("Sales")
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("Sales_Dashboard.png", dpi=300, bbox_inches='tight')
plt.show()
