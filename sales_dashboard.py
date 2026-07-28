import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())

print(df.describe())

sales_by_category = df.groupby('Category')['Sales'].sum()
print(sales_by_category)

sales_by_region = df.groupby('Region')['Profit'].sum()
print(sales_by_region)

sales_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
print(sales_by_state)

sales_by_segment = df.groupby('Segment')['Sales'].sum()
print(sales_by_segment)

plt.figure()
sales_by_category.plot(kind='bar', title='Sales by Category', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.savefig('Sales_by_category.png')
plt.close()

plt.figure()
sales_by_region.plot(kind='bar',title='Sales by Region',color='red')
plt.xlabel('region')
plt.ylabel('sales')
plt.xticks(rotation=0)
plt.savefig('Sales_by_region.png')
plt.close()

plt.figure()
sales_by_state.plot(kind='bar',title='Sales by state',color='green')
plt.xlabel('state')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.savefig('top_10_states.png')
plt.close()

plt.figure()
sales_by_segment.plot(kind='pie',title='Sales by segment',color='grey',shadow=True)
plt.xlabel('segment')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.savefig('sales_by_segment.png')
plt.close()