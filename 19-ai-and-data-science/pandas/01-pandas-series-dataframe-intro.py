import numpy as np 
import pandas as pd

# # Creating A Pandas Series With Custom Index
# data = [10, 20, 30 ,40]
# index = ['a', 'b', 'c', 'd']
# series = pd.Series(data, index=index)

# print(f"Series With Custom Index : \n{series}")

# # Creating A Dataframe From Dictionary
# data_dict = {
#     "Name" : ['Alice', "Bob", "Charlie"],
#     "Age" : [25, 30, 35],
#     "Salary" : [50000, 60000, 70000]
# }
# data_frame = pd.DataFrame(data_dict)
# print(f"Dataframe From Dictionary : \n{data_frame}")

# # Creating A Dataframe From A List Of Dictionaries
# data_list = [
#     {'Name' : 'Dave', 'Age' : 40, 'Salary' : 80000},
#     {'Name' : 'Eve', 'Age' : 45, 'Salary' : 90000}
# ]

# df_frame_list = pd.DataFrame(data_list)
# print(f"Dataframe From List Of Dictionaries : \n{df_frame_list}")

# # Creating Dataframe From Numpy Arrays
# arr_data = np.array([[1, 2], [3, 4], [5, 6]])
# columns = ['Coulmn1', 'Coulmn2']
# df_from_arr = pd.DataFrame(arr_data, columns=columns)
# print(f"Dataframe From Numpy Arrays: \n{df_from_arr}")

# # Creating Dataframe With Custom Index And Columns
# data_ = {
#     'column1' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#     'column2' : pd.Series([4, 5, 6], index=['a', 'b', 'c'])
# }
# custom_df = pd.DataFrame(data_) 
# print(f"Custom Dataframe : \n{custom_df}")


# # Example Of Importing Data From CSV File
df = pd.read_csv(r'C:\Users\eyad0\Documents\Thanaweya_2025.csv')
# print(f"First 5 Rows : \n{df.head()}")
# print(f"Dataframe Info : \n")
# df.info()


# # Create A Simple Dataframe And Save It As CSV
# simple_df = pd.DataFrame({
#     'A' : np.random.randint(1, 10, size=5),
#     'B' : np.random.rand(5),
#     'C' : ['foo', 'bar','baz' ,'qux', 'quux']
# })

# simple_df.to_csv(r'C:\Users\eyad0\Documents\sample_data.csv', index=False)

# # Load Tha Data Back
# df = pd.read_csv(r'C:\Users\eyad0\Documents\sample_data.csv')
# print(f"Loaded Data: {df}")

print(f"First 5 Rows: \n{df.head(5)}")
print(f"Last 5 Rows: \n{df.tail(5)}")

print(f"Dataframe inf : \n")
df.info()

print(f"Summary Statistics: \n{df.describe()}")

# Checking Data Types
print(f"Data Types: \n{df.dtypes}")

# # Value Counts For Column 'A'
# print(f"Value Counts For Column 'A': \n{df['A'].value_counts()}")