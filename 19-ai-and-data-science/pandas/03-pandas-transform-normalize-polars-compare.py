import numpy as np
import pandas as pd
import time
 

# Create A Sample DataFrame
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
sales = np.random.randint(1000, 5000, size=(len(dates)))
expenses = np.random.randint(500, 3000, size=(len(dates)))

# time_series_df = pd.DataFrame({
#     'Date' : dates,
#     'Sales' : sales,
#     'Expenses' : expenses
# })

# time_series_df.set_index('Date', inplace=True)
# print(f"Original DataFrame : \n{time_series_df}")

# # Tanspose
# transposed_df = time_series_df.T
# print(f"Tansposed DataFrame : \n{transposed_df}")

# # Sorting By Index 
# sorted_df = time_series_df.sort_index(ascending=False)
# print(f"Sorted Dataframe : \n{sorted_df}")

# # Adding A New Column
# time_series_df['Profit'] = time_series_df['Sales'] - time_series_df['Expenses']
# print(f"Dataframe With Profit Column : \n{time_series_df}")

# # Dropping A Column
# time_series_df = time_series_df.drop('Expenses', axis=1)
# print(f"Dataframe Without Expenses Column : \n{time_series_df}")


# # Create Data Range
# dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
# time_series_df_ = pd.DataFrame({
#     'Sales' : np.random.randint(100, 200, size=(len(dates))),
#     'Expenses' : np.random.randint(50, 100, size=(len(dates)))
    
# }, index=dates)

# print(f"Time Series Dataframe: \n{time_series_df_}")

# # Access Data By Date
# print(f"Data On 2024-01-05: \n{time_series_df_.loc['2024-01-05']}")


# large_arr = np.random.randint(0, 1000000, size=1000000)

# start_time = time.time()
# result_loop = np.zeros_like(large_arr)
# for i in range(len(large_arr)):
#     result_loop[i] = large_arr[i] * 2
    
# print(f"Time With Loop : \n{time.time() - start_time}")


# # Using Vectorized Operation
# start_time = time.time()
# result_vectorized = large_arr * 2
# print(f"Time With Vectorization: \n{time.time() - start_time}")

employee_data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [25, 30, 35, 28],
    'Salary' : [50000, 60000, 70000, 80000]
}

employee_df = pd.DataFrame(employee_data)

# Using Numpy To Calculate Bonus
employee_df['Bonus'] = np.where(employee_df['Age'] > 28, employee_df['Salary'] *0.1, employee_df['Salary'] *0.5)
print(f"Employee Data With Bonus : \n{employee_df}")



# Log-Transform The Salary
employee_df['Salary_Log'] = np.log(employee_df['Salary'])
print(f"Employee Data With log-Transformed Salary: \n{employee_df}")

# One-Hot Encode 'Name' Column
name_dummies = pd.get_dummies(employee_df['Name'], prefix='Name')
employee_df = pd.concat([employee_df, name_dummies], axis=1)
print(f"Employee Data With One-Hot Encoded Names : \n{employee_df}")

# Normalize 'Salary' Column
employee_df['Salary_norm'] = (employee_df['Salary'] - employee_df['Salary'].mean()) / employee_df['Salary'].std()
print(f"Employee Data With Normalized Salary : \n{employee_df}")


####################################################################################################################

import polars as pl

# Creating Dataframes In Polars And Pandas 
data = {'col1' : [1, 2, 3], 'col2' : [4, 5, 6]}
df_polars = pl.DataFrame(data)
df_pandas = pd.DataFrame(data)

print(f"Polars Dataframe : \n{df_polars}")
print(f"Pandas Dataframe : \n{df_pandas}")

# Generate Large Dataset
data_large = {'col1' : np.random.rand(1000000), 'col2' : np.random.rand(1000000)}
df_pandas_large = pd.DataFrame(data_large)
df_polars_large = pl.DataFrame(data_large)


# Pandas Operation
start_time = time.time()
df_pandas_large['nul'] = df_pandas_large['col1'] * df_pandas_large['col2']
print(f"Pandas Operation Time : \n{time.time() - start_time}")


# Polars Operation
start_time = time.time()
df_polars_large['nul'] = df_polars_large['col1'] * df_polars_large['col2']
print(f"Polars Operation Time : \n{time.time() - start_time}")

