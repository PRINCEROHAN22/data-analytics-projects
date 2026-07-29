import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st 

st.title("Sales Dashboard")
st.write("Analysis of Superstore sales data")

df = pd.read_csv("SampleSuperstore.csv")

st.write(df.head())

st.write(df.describe())

sales_by_category = df.groupby('Category')['Sales'].sum()
st.write(sales_by_category)

sales_by_region = df.groupby('Region')['Profit'].sum()
st.write(sales_by_region)

sales_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
st.write(sales_by_state)

sales_by_segment = df.groupby('Segment')['Sales'].sum()
st.write(sales_by_segment)

plt.figure()
sales_by_category.plot(kind='bar', title='Sales by Category', color='skyblue')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.savefig('Sales_by_category.png')
st.pyplot(plt)
plt.close()

plt.figure()
sales_by_region.plot(kind='bar',title='Sales by Region',color='red')
plt.xlabel('region')
plt.ylabel('sales')
plt.xticks(rotation=0)
plt.savefig('Sales_by_region.png')
st.pyplot(plt)
plt.close()

plt.figure()
sales_by_state.plot(kind='bar',title='Sales by state',color='green')
plt.xlabel('state')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.savefig('top_10_states.png')
st.pyplot(plt)
plt.close()

plt.figure()
sales_by_segment.plot(kind='pie',title='Sales by segment',color='grey',shadow=True)
plt.xlabel('segment')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.savefig('sales_by_segment.png')
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(x=df['Sales'],y=df['Profit'],color="yellow")
plt.xlabel('sales')
plt.ylabel('profit')
plt.xticks(rotation=45)
plt.savefig('sales_vs_profit.png')
st.pyplot(plt)
plt.close

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
highest_profit_category = df.groupby('Category')['Profit'].idxmax()
lowest_profit_region = df.groupby('Region')['Profit'].idxmin()

st.write(f"\nTotal Number Of Sales Across All Orders : {total_sales}")
st.write(f"\nTotal Profit Across All Orders : {total_profit}")
st.write(f"\nHighest Profit Among Category : {highest_profit_category}")
st.write(f"\nLowest Profit Among Region : {lowest_profit_region}")