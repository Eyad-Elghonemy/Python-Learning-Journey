import numpy as np
import random

# myFile = open(r"C:\Users\eyad0\Documents\binary_file.csv", 'a')

# myFile.write("1.100000000000000089e+00,2.200000000000000178e+00,3.299999999999999822e+00\n")
# myFile.write("4.400000000000000355e+00,5.500000000000000000e+00,6.599999999999999645e+00\n")
# myFile.write("7.700000000000000178e+00,8.800000000000000711e+00,9.000000000000000355e+00\n")

# data = np.loadtxt(r"C:\Users\eyad0\Documents\binary_file.csv", delimiter=',')
# print("Loaded Data: \n", data)

# sample_data = np.random.rand(3, 2)
# print(sample_data)
# np.savetxt(r"C:\Users\eyad0\Documents\Random_Data.csv", sample_data, delimiter=',', fmt='%.2f')

# data2 = np.loadtxt(r"C:\Users\eyad0\Documents\Random_Data.csv", delimiter=',')
# print("Loaded Data 2 : \n", data2)


# arr = np.array([10, 20, 30, 40, 50])
# print(f"Original Array: {arr}")

# # Indexing
# print(f"Element At Index 1 : {arr[1]}")

# # Slicing
# print(f"Slice From Index 1 to 3: {arr[1:4]}")

# # Modifying a Slice
# arr_slice = arr[1:4]
# arr_slice[0] = 25

# print(f"Modified Sliced Array : {arr_slice}")
# print(f"Array After Slice Modification : {arr}")

# # Concatenation
# arr2 = np.array([60, 70])
# concat_arr = np.concatenate((arr, arr2))

# print(f"concatenatenation Array : {concat_arr}")

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Arithmatic Operations
# print(f"Addition : {a + b}")
# print(f"Subtraction : {a - b}")
# print(f"Multiplication : {a * b}")
# print(f"Division : {a / b}")

# # Scaler Operations
# print(f"Scaler Addition : {a + 10}")
# print(f"Scaler Multiplication : {a * 3}")

# # Broadcasting Ex
# c = np.array([[1], [2], [3]])
# d = np.array([4, 5, 6])
# print(f"Broadcasting Multiplication : {c * d}")


# # Boolean Indexing Example
# a = np.array([1, 2, 3, 4, 5])
# mask = (a > 2) & (a < 5)
# filtered_array = a[mask]
# print(f"Mask : {mask}")
# print(f"Filtered Array : {filtered_array}")

# # Modifying Elements Based On Conditions
# a[a>3] = 10
# print(f"Array After Modification : {a}")




# # Casting 
# float_arr = np.array([1, 2, 3, 4, 0], dtype='float64')
# print(f"Float Array : {float_arr}")
# print(f"Data Type : {float_arr.dtype}")

# # Casting To Integer
# int_arr = float_arr.astype('int32')
# print(f"Casted To Integer: {int_arr}")
# print(f"Data Type : {int_arr.dtype}")

# # Casting To Boolean
# bool_arr = float_arr.astype('bool')
# print(f"Casted To Boolean: {bool_arr}")
# print(f"Data Type : {bool_arr.dtype}")


# # Random Number Generation
# np.random.seed(42)


# # Uniform Distribution (0, 1)
# Uniform_Arr = np.random.rand(5)
# print(f"Uniform Raandom Array : {Uniform_Arr}")

# # Normal Distribution (mean=0, std=1)
# random_arr = np.random.randn(5)
# print(f"Noramal Array : {random_arr}")

# # Random Integers Between Low (inclusive) and High (exclusive)
# random_ints = np.random.randint(1, 100, size=5)
# print(f"Random Integers: {random_ints}")