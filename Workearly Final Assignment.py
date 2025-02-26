import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for the timeframe 2016-2019
df = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]

# Clean data: drop rows with missing values in relevant columns
df = df.dropna(subset=['zip_code', 'store_number', 'item_description', 'bottles_sold'])

# Most popular item per zipcode by bottles sold
popular_items = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
most_popular_items = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

# Sales percentage per store by bottles sold
total_bottles_per_store = df.groupby('store_number')['bottles_sold'].sum().reset_index()
total_bottles = total_bottles_per_store['bottles_sold'].sum()
total_bottles_per_store['sales_percentage'] = (total_bottles_per_store['bottles_sold'] / total_bottles) * 100

# Visualization: Sales percentage distribution
plt.figure(figsize=(12, 6))
sns.barplot(x='store_number', y='sales_percentage', data=total_bottles_per_store)
plt.xticks(rotation=90)
plt.title('Sales Percentage per Store (2016-2019) - Bottles Sold')
plt.ylabel('Sales Percentage (%)')
plt.xlabel('Store Number')
plt.show()

# Scatter plot with Matplotlib for most popular items per zipcode
plt.figure(figsize=(12, 6))
plt.scatter(most_popular_items['zip_code'], most_popular_items['bottles_sold'], color='blue')
for i, txt in enumerate(most_popular_items['zip_code']):
    plt.annotate(txt, (most_popular_items['zip_code'].iloc[i], most_popular_items['bottles_sold'].iloc[i]))
plt.title('Most Popular Items per Zipcode (2016-2019) - Bottles Sold')
plt.xlabel('Zipcode')
plt.ylabel('Bottles Sold')
plt.show()

# Scatter plot with Plotly
fig = px.scatter(most_popular_items, x='zip_code', y='bottles_sold', size='bottles_sold', color='item_description',
                 title='Most Popular Items per Zipcode (2016-2019) - Bottles Sold', labels={'bottles_sold': 'Bottles Sold', 'zip_code': 'Zipcode'})
fig.show()

# Display most popular items per zipcode
print('Most Popular Items per Zipcode (2016-2019):')
print(most_popular_items)

# Display sales percentage per store
print('\nSales Percentage per Store (2016-2019):')
print(total_bottles_per_store[['store_number', 'sales_percentage']])
