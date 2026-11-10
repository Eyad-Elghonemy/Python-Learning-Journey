import numpy as np

# # Linear Algebra
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# # Matrix Multiplication
# matrix_prod = np.dot(a, b)
# print(f"Matrix_Prod: \n{matrix_prod}")

# # USing @ Operator
# matrix_prod2 = a @ b
# print(f"Matrix_Prod: \n{matrix_prod}")

# # Transpose
# print(f"Transpose Of Matrix A : \n{a.T}")



# # Determinant
# matrix = np.array([[2, 1], [1, 2]])
# determinant = np.linalg.det(matrix)
# print(f"Determinant Of Matrix : {determinant}")


# # Inverse
# inverse_matrix = np.linalg.inv(matrix)
# print(f"Inverse Of Matrix : \n{inverse_matrix}")

# # Eigenvalues & Eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(matrix)
# print(f"Eigenvalues : \n{eigenvalues}")
# print(f"Eigenvectors : \n{eigenvectors}")



# a = np.array([1, 4, 16, 25])

# sqrt_arr = np.sqrt(a)
# exp_arr = np.exp(a)
# log_arr = np.log(a)


# print(f"Original Array : \n{a}")
# print(f"Square Root Array : \n{sqrt_arr}")
# print(f"Exponential Array : \n{exp_arr}")
# print(f"Logarithm Array : \n{log_arr}")


# A = np.array([[3, 1], [1, 2]])
# B = np.array([9, 8])

# # Solving Linear Equations
# sol = np.linalg.solve(A, B)
# print(f"Solution X: {sol}")

# # Verification
# ver = A @ sol
# print(f"Verification : {ver}")
# print(f"B : {B}")


# arr = np.arange(12)
# print(f"Original Array : \n{arr}")

# # Reshape To 3x4
# reshaped_arr = arr.reshape(3,4)
# print(f"Reshaped 3x4 Array : \n{reshaped_arr}")

# # Reshape To 2x2x3
# reshaped_arr_3d = arr.reshape(2, 2, 3)
# print(f"Reshaped 2x2x3 Array : \n{reshaped_arr_3d}")

# # Flatten The Array
# flat_arr = reshaped_arr_3d.flatten()
# print(f"Flatten Array : \n{flat_arr}")


# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# # Vertical Stacking
# v_stack = np.vstack((arr1,arr2))
# print(f"Vertical Stack : \n{v_stack}")

# # Horizontal Stacking
# h_stack = np.hstack((arr1,arr2))
# print(f"Horizontal Stack : \n{h_stack}")

# # Splitting Arrays
# split_arr = np.hsplit(h_stack, 2)
# print("Split Arrays: \n")
# for i, arrr in enumerate(split_arr):
#     print(f"Array {i}: \n{arrr}")


# arr = np.arange(10)
# indices = [2, 5, 3]
# fancy_indexed_elements = arr[indices]

# print(f"Original Array : \n{arr}")
# print(f"Indices : \n{indices}")
# print(f"Fancy Indexed Elements : \n{fancy_indexed_elements}")

# # Using Boolean Array For Indexing
# bool_indices = arr % 2 == 0      # --> Even Nums
# even_elements = arr[bool_indices]
# print(f"Boolean Indices : \n{bool_indices}")
# print(f"Even Elements : \n{even_elements}")