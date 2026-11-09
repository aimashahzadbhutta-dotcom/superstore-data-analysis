import pandas as pd
import numpy as np

print("NUMPY SALES ANALYSIS\n")
df = pd.read_csv("train.csv")
Sales = df["Sales"]
array = np.array(Sales)
print("Array properties: ")
print(f"Data type: {array.dtype}\n Shape: {array.shape}\n No. of dimensions: {array.ndim}\n Array size: {array.size}")

print("\nStatistics of Sales")
mean = array.mean()
print("Mean: ", mean)
print("Median: ", np.median(array ))
print("Standard Deviation: ", array.std())
print("Minumum: ", array.min())
print("Maximum: ", array.max())

greater_sales = (array > mean)
print("\nNumber of sales values above mean: ", greater_sales.sum())

Greater_sales = array[array > mean]
new_array = np.array(Greater_sales)
print("Above-mean sales :", new_array)
print("Count: ", len(new_array))
print("Mean: ", new_array.mean())
print("Maximum: ", new_array.max())