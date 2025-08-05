import numpy as np

# Arrays:
list = np.array([1,2,3,4,5])
print(list)
print(list[:3])
print(list[3:])

# Matrices:

matrice = np.array([[1,2,3],[4,5,6]])
print(matrice)

print(matrice.T) # Transversal

print(matrice[1,2]) # Find a especific value within the matrix (1 - row, 2 - column) - we can't forget that the index initiates with 0

# Array Atributes

#1. Ndim (Number of dimensions)

print(f"The number of dimenions of the matrix : {matrice.ndim}")

#2. Shape of a matrix

print(f"The shape of the matrix : {matrice.shape}")

#3. Number of attributes

print(f"The number of attributes : {matrice.size}")

#4. dType (data type)

print(f"The type of the matrix : {matrice.dtype}")

#5. Sort & Concatenate

print(np.sort(list))

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(np.concatenate((a,b)))

x = np.array([[1,2], [3,4]])
y = np.array([[5,6]])

print(np.concatenate((x,y), axis = 0))