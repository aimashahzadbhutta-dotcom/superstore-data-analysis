import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("train.csv")
Sales = df["Sales"]

array = np.array(Sales)
# median = np.median(array)
# print("Median: ", median)
# std = array.std()
# print("variance: ", std**2)
# print(Sales.describe())
# Q1 = np.percentile(array, 25)
# Q2 = np.percentile(array, 50)
# Q3 = np.percentile(array, 75)
# IQR = Q3-Q1
# print("Interquartile Range: ", IQR)
# L_Bndry = Q1 - 1.5 * IQR
# U_Bndry = Q3 + 1.5 * IQR
# print("Lower Boundary: ", L_Bndry)
# print("Upper Boundary: ", U_Bndry)
# values_above_U_Bndry = (array>U_Bndry)
# print("Outlier Sales (boolean)", values_above_U_Bndry)
# n_U_outliers = (array>U_Bndry).sum()
# print("Number of outlier sales: ", n_U_outliers)
# Outlier_Sales = df[df["Sales"]>U_Bndry]["Sales"]
# print("Outlier Sales: ", Outlier_Sales)
# Top_outlier_sales = Outlier_Sales.sort_values(ascending=False)
# Top_10 = Top_outlier_sales.head(10)
# print("Top 10 outlier sales: ", Top_10)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["year"] = df["Order Date"].dt.year
df2 = df.groupby("year").agg(Total_Sales = ('Sales','sum'), Average_Sale=('Sales','mean')).reset_index()
Total_Sales = df2["Total_Sales"]
# print(Total_Sales)
# plt.style.use("ggplot")
# plt.plot(Total_Sales.index, Total_Sales.values, color='blue', linewidth=1, marker='o', label='Trend of Sales')
# plt.legend()
# plt.title("Total Sales by year", fontweight='bold')
# plt.xlabel("Year")
# plt.xticks(Total_Sales.index)
# plt.ylabel("Total Sales")
# plt.tight_layout()
# plt.show()
print(df2.corr())