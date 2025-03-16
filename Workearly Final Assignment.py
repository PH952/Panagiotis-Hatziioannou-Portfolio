"""import pandas as pd
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
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for the timeframe 2016-2019
df = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]

# Clean data: drop rows with missing values in relevant columns
df = df.dropna(subset=['zip_code', 'store_name', 'item_number', 'bottles_sold'])

# Most popular item per zipcode by bottles sold
popular_items = df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
most_popular_items = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

# Sales percentage per store by bottles sold
total_bottles_per_store = df.groupby('store_name')['bottles_sold'].sum().reset_index()
total_bottles = total_bottles_per_store['bottles_sold'].sum()
total_bottles_per_store['sales_percentage'] = (total_bottles_per_store['bottles_sold'] / total_bottles) * 100

# Display preview of modified dataset
print('Preview of Modified Dataset:')
print(df[['zip_code', 'item_number', 'bottles_sold']].head(15))

# Visualization: Sales percentage distribution with Matplotlib
plt.figure(figsize=(12, 6))
total_bottles_per_store = total_bottles_per_store.sort_values(by='sales_percentage', ascending=False)
plt.barh(total_bottles_per_store['store_name'].astype(str), total_bottles_per_store['sales_percentage'], color='steelblue')
plt.xlabel('% Sales by store')
plt.title('Sales Percentage by Store (2016-2019) - Bottles Sold')
plt.gca().invert_yaxis()

# Add data labels
for i, v in enumerate(total_bottles_per_store['sales_percentage']):
    plt.text(v, i, f"{v:.2f}", color='black', va='center')

plt.show()

# Scatter plot with Plotly
fig = px.scatter(most_popular_items, x='zip_code', y='bottles_sold', size='bottles_sold', color='item_number',
                 title='Most Popular Items per Zipcode (2016-2019) - Bottles Sold', labels={'bottles_sold': 'Bottles Sold', 'zip_code': 'Zipcode'})
fig.show()

# Display most popular items per zipcode
print('Most Popular Items per Zipcode (2016-2019):')
print(most_popular_items)

# Display sales percentage per store
print('\nSales Percentage per Store (2016-2019):')
print(total_bottles_per_store[['store_name', 'sales_percentage']])
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for the timeframe 2016-2019
df = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]

# Clean data: drop rows with missing values in relevant columns
df = df.dropna(subset=['zip_code', 'store_name', 'item_number', 'bottles_sold'])

# Most popular item per zipcode by bottles sold
popular_items = df.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
most_popular_items = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

# Sales percentage per store by bottles sold
total_bottles_per_store = df.groupby('store_name')['bottles_sold'].sum().reset_index()
total_bottles = total_bottles_per_store['bottles_sold'].sum()
total_bottles_per_store['sales_percentage'] = (total_bottles_per_store['bottles_sold'] / total_bottles) * 100

# Display preview of modified dataset
print('Preview of Modified Dataset:')
print(df[['zip_code', 'item_number', 'bottles_sold']].head(15))

# Visualization: Sales percentage distribution with Matplotlib
plt.figure(figsize=(12, 6))
total_bottles_per_store = total_bottles_per_store.sort_values(by='sales_percentage', ascending=False)
plt.barh(total_bottles_per_store['store_name'].astype(str), total_bottles_per_store['sales_percentage'], color='steelblue')
plt.xlabel('% Sales by store')
plt.title('Sales Percentage by Store (2016-2019) - Bottles Sold')
plt.gca().invert_yaxis()

# Add data labels
for i, v in enumerate(total_bottles_per_store['sales_percentage']):
    plt.text(v, i, f"{v:.2f}", color='black', va='center')

plt.show()

# Scatter plot with Plotly (Revised)
fig = px.scatter(most_popular_items,
                 x='zip_code',
                 y='bottles_sold',
                 size='bottles_sold',
                 color='bottles_sold',  # Color by bottles sold instead of item_number
                 color_continuous_scale='plasma',  # Adjusted to a continuous color scale similar to your image
                 size_max=60,  # Ensures the bubble size does not get too large
                 title='Most Popular Items per Zipcode (2016-2019) - Bottles Sold',
                 labels={'bottles_sold': 'Bottles Sold', 'zip_code': 'Zipcode'})

# Update layout for more resemblance to the example chart
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Jittered Index',  # Customizing the color bar label
        tickvals=[10, 20, 30, 40, 50, 60],  # Custom ticks for the color scale
        ticktext=['10', '20', '30', '40', '50', '60'],  # Custom tick text
    ),
    plot_bgcolor='rgba(240, 240, 240, 0.9)',  # Set background color of the plot
    xaxis_title='Zipcode',  # Title for the x-axis
    yaxis_title='Bottles Sold',  # Title for the y-axis
    title_x=0.5,  # Center the title
    title_y=0.95,  # Adjust the title position
    showlegend=False,  # Disable the legend to match the image
    xaxis=dict(
        showgrid=True,  # Show grid lines for better readability
        zeroline=False  # Remove the line at x=0
    ),
    yaxis=dict(
        showgrid=True,  # Show grid lines for better readability
        zeroline=False  # Remove the line at y=0
    )
)

fig.show()

# Display most popular items per zipcode
print('Most Popular Items per Zipcode (2016-2019):')
print(most_popular_items)

# Display sales percentage per store
print('\nSales Percentage per Store (2016-2019):')
print(total_bottles_per_store[['store_name', 'sales_percentage']])
