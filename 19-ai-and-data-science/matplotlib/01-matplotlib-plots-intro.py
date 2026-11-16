import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
 

# # Sample Data
# dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
# sales = [12, 18, 20, 25, 22, 30, 35, 40, 38, 32, 28, 36]

# # Line Plot
# plt.plot(dates, sales)
# # plt.show()

# # Sample Data
# adv_bud = np.random.randint(10, 50, 20)
# sales = adv_bud + np.random.normal(0, 5, 20)

# # Scaler Plot
# plt.figure()
# plt.scatter(adv_bud, sales)
# plt.show()



# # Sample Data
# categories = ['A', 'B', 'C', 'D']
# values = [25, 40, 35, 50]

# # Bar Plot
# plt.bar(categories, values)
# # plt.show()

# # Sample Data
# np.random.seed(42)
# data = np.random.normal(loc = 50, scale = 10, size=10)

# plt.figure()
# # Histogram
# plt.hist(data)
# plt.show()

# # Sample Data
# data = pd.DataFrame({
#     'Category' : ['A', 'B', 'C', 'D'] *20,
#     'Values' : np.random.randint(10, 50, 80)
# })

# # Box Plot
# plt.boxplot([data[data['Category'] == cat]['Values'] for cat in data['Category'].unique()], labels=data['Category'].unique())
# plt.show()


# # Sample Data
# y = np.array([35, 25, 25, 15])
# mylabels = ['Apples', 'Bananas', 'Cherries', 'Dates']

# plt.figure()
# # Pie plot
# plt.pie(y, labels=mylabels)
# plt.show()

###################################################

# Sample Data
dates = pd.date_range(start='2023-01-01', periods=12, freq='ME')
sales_product_a = [12, 18, 20, 25, 22, 30, 35, 40, 38, 32, 28, 36]
sales_product_b = [15, 17, 23, 20, 26, 29, 33, 37, 39, 30, 27, 34]

# # Custom Line Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a)
# plt.show()

# # Labels
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a)
plt.title("Monthly Sales Comparison", fontsize = 16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Sales", fontsize=14)
# plt.show()

# # Custom Line Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a, label='Product A')
plt.plot(dates, sales_product_b, label='Product B')
plt.title('Monthly Sales Comparison', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.grid(True)
# plt.show()

# # Custom Line Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a, marker='o', color='b', linestyle='-', linewidth=2, label='Product A')
plt.plot(dates, sales_product_b, marker='s', color='g', linestyle='--', linewidth=2, label='Product B')
plt.title('Monthly Sales Comparison', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
# plt.show()


# # Custom Line Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a, marker='o', color='b', linestyle='-', linewidth=2, label='Product A')
plt.plot(dates, sales_product_b, marker='s', color='g', linestyle='--', linewidth=2, label='Product B')
plt.title('Monthly Sales Comparison', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.style.use('ggplot')
plt.show()

# # Custom Line Plot
plt.figure(figsize=(12, 6))
plt.plot(dates, sales_product_a, marker='o', color='b', linestyle='-', linewidth=2, label='Product A')
plt.plot(dates, sales_product_b, marker='s', color='g', linestyle='--', linewidth=2, label='Product B')
plt.title('Monthly Sales Comparison', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.style.use('dark_background')
plt.show()

# print(plt.style.available)

plt.figure(figsize=(12,6))
plt.plot(dates, sales_product_a, marker='o', linestyle='-', linewidth=2, label='Product A')
plt.title("Monthly Sales With Annotation")
plt.xlabel('Month')
plt.ylabel('Sales')
plt.annotate('Highest Sales', xy=(dates[7], sales_product_a[7]), xytext=(dates[4], sales_product_a[6] + 5), 
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.grid(True)
plt.show()