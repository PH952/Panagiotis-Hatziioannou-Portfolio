import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ---- Load dataset ----
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # coerce errors to NaT

# Drop rows with missing key fields
df = df.dropna(subset=['date', 'zip_code', 'store_name', 'item_number', 'bottles_sold', 'sale_dollars'])

# Filter 2016–2019
df = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]

# ---- Remove invalid sales ----
df = df[df['sale_dollars'] > 0]
df = df[df['bottles_sold'] > 0]

# ---- Most popular item per ZIP code ----
popular_items = df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
most_popular_items = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]
most_popular_items = most_popular_items.reset_index(drop=True)
most_popular_items['jittered_index'] = most_popular_items.index

# ---- Sales percentage per store (in dollars) ----
store_sales = df.groupby('store_name')['sale_dollars'].sum().reset_index()
total_sales = store_sales['sale_dollars'].sum()
store_sales['sales_percentage'] = (store_sales['sale_dollars'] / total_sales) * 100

# Sort descending
store_sales = store_sales.sort_values(by='sales_percentage', ascending=False)

# ---- Bar Chart: Top 15 stores ----
top_15_stores = store_sales.head(15)

plt.figure(figsize=(10, 6))
bars = plt.barh(top_15_stores['store_name'], top_15_stores['sales_percentage'], color='steelblue')
plt.xlabel('%Sales')
plt.ylabel('%Sales by store')
plt.title('')
plt.gca().invert_yaxis()

# Add percentage labels on the right of bars - matching screenshot format
for bar, v in zip(bars, top_15_stores['sales_percentage']):
    plt.text(v + 0.2, bar.get_y() + bar.get_height()/2, f"{v:.2f}", color='black', va='center', fontsize=10)

# Set x-axis limits and ticks to match screenshot
plt.xlim(0, 20)
plt.xticks([0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0])

# Remove top and right spines to match screenshot style
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# ---- Plotly Scatter: Most Popular Items per ZIP ----
fig = px.scatter(
    most_popular_items,
    x='jittered_index',
    y='bottles_sold',
    size='bottles_sold',
    color='jittered_index',
    hover_data=['zip_code', 'bottles_sold', 'item_number'],
    color_continuous_scale='plasma',
    size_max=60,
    title='Most Popular Items per Zipcode (2016–2019) - Bottles Sold',
    labels={'bottles_sold': 'Bottles Sold', 'jittered_index': 'jittered_index'}
)

fig.update_xaxes(tickmode='linear', dtick=20, tickformat=',d')
fig.show()

# ---- Print Outputs ----
print('Most Popular Items per Zipcode (2016–2019):')
print(most_popular_items[['zip_code','item_number','bottles_sold']])

print('\nSales Percentage per Store (2016–2019):')
print(store_sales[['store_name', 'sales_percentage']])

# ---- Debug: Print exact values for top 15 stores to verify against screenshot ----
print('\nTop 15 Stores - Exact Values:')
for i, row in top_15_stores.iterrows():
    print(f"{row['store_name']}: {row['sales_percentage']:.2f}%")