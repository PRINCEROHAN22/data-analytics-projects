import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())

print(df.describe())

sales_by_category = df.groupby('Category')['Sales'].sum()
print(sales_by_category)

sales_by_category.plot(kind='bar', title='Sales by Category', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.show()
