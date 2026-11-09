import pandas as pd

df = pd.read_csv("train.csv")

print("Information about most frequent customer: \n")

unique_ids = df["Customer ID"].nunique()
print("Total Customers: ", unique_ids)

print("Most repeated customer:")
Most_rep_id = df["Customer ID"].value_counts().idxmax()
Top_customer = df.loc[df["Customer ID"] == Most_rep_id, ['Customer Name','Customer ID']].iloc[0]
print(Top_customer)

total_purchase = df.loc[df["Customer ID"] == Most_rep_id, 'Sub-Category'].count()
print("Number of items most frequent cumtomer purchased: ", total_purchase)
print("Information about Category and Sub-Category of items this customer purchased: ")
group = df[df["Customer ID"] == Most_rep_id].groupby("Category")["Sub-Category"]
for a, l in group:
    print(a)
    print(l.unique())

print("Information about overall Sales and Sold items: \n")

print("Average Sales: ", df["Sales"].mean())

print("Number of categories of items availabe to sale: ", df["Category"].nunique())
print("Categories: ", df["Category"].unique())
Top_sold_Category = df["Category"].value_counts().idxmax()
print("Top sold Category: ",Top_sold_Category)
Sales = df.loc[df["Category"] == Top_sold_Category, 'Sales'].sum()
print("Total sale of top sold Category: ", Sales)

Sub_Category = df.loc[df["Category"] == Top_sold_Category, 'Sub-Category']
print("Sub-Categories of top sold Category: ",Sub_Category.unique())
print("Total number of Sub-Categories available: ",Sub_Category.nunique())
Top_sold_subcategory = df["Sub-Category"].value_counts().idxmax()
print("Top sold sub-Category: ", Top_sold_subcategory)
Total_sales_subcategory = df.loc[df["Sub-Category"] == Top_sold_subcategory, 'Sales'].sum()
print("Total Sales of Top Sold Sub-Category: ", Total_sales_subcategory)
Top_sold_item = df["Sub-Category"].value_counts().idxmax()
print("Top sold item:",Top_sold_item)
number = df.loc[df["Sub-Category"] == Top_sold_item, 'Sales'].sum()
print("Total sale of top sold item: ",number)
print("\n")

print("Detail of Region with maximum sale: ")
region = df.groupby("Region")["Sales"].sum()
print(region)
max_sale = region.max()
region_with_max_sale = region[region == max_sale]
print("Region with top sales: ", region_with_max_sale.idxmax())
print("Total sales: ", region_with_max_sale.iloc[0])

print("Detail of customer with maximum sale: ")

b = df.groupby(['Customer ID','Customer Name'])['Sales'].sum()
m = b.max()
row = b[b == m]
print("Customer Name   Customer ID \n", row.idxmax())
print("Total Sales: ", row.iloc[0])

print("\n")
print("Ship Modes and their usage: ")
top_ship_mode = df["Ship Mode"].value_counts()
print(top_ship_mode)
print("Most frequent Ship Modes: ", top_ship_mode.idxmax())

