import numpy as np

# 1. Create a vector with values ranging from 3 to 20
vector_1 = np.random.randint(3, 20, 10)
# print(np.random.randint.__doc__)
print(vector_1)

# 2. Create a 3x3 identity matrix
vector_2 = np.identity(3, dtype=int)
# print(np.identity.__doc__)
print(vector_2)

# 3. Create a random vector of size 10 and sort it
vector_3 = np.random.randint(1, 100, size=10)
print(vector_3)
vector_3 = np.sort(vector_3)
print(vector_3)

# 4.Create a random 1-D matrix, Convert 1-D to 3-D matrix
vector_4 = np.random.randint(1, 50, 9)
print(vector_4)
vector_4 = np.reshape(vector_4, (3, 3))
print(vector_4)

# 5. Create 2 numpy arrays as matrices (random) , Print the result of multiplying the 2 matrices (as a numpy array)
matrix_1 = np.random.randint(1, 10, (3, 4))
matrix_2 = np.random.randint(1, 10, (4, 2))
print(matrix_1 @ matrix_2)

# 6. Create a 5*5 matrix (random ) , print the first three rows and first 2 columns
matrix_3 = np.random.randint(1, 10, (5, 5))
print(matrix_3)
print("First three rows: ")
print(matrix_3[:3][::])
print("First two columns: ")
print(matrix_3.shape[0])
for i in range(matrix_3.shape[0]):
    print(matrix_3[i][:2])
# 7. Create a 5*10 matrix , print subtract the mean of each row of a matrix
matrix_4 = np.random.randint(1, 10, (5, 10))
print(matrix_4)
matrix_4 = matrix_4 - matrix_4.mean(axis=1, keepdims=True)
print(matrix_4)