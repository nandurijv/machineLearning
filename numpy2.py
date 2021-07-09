
import numpy as np
arr = np.arange(0,10)

print(arr[8])#indexing
print(arr[:9])#slicing
print(arr[1:6:2])

arr[0:5] = 100
print(arr)

#sliced array is actually a view of the original
#changes made to sliced array changes original array

array = np.arange(0,11)
array_slice = array[0:6]
array_slice[:] = 99
print(array_slice)
print(array)

#use .copy() to avoid making any changes to original
array_copy = array.copy()
array_copy[:] = 999
print(array)
print(array_copy)

#indexing a two dimensional array/matrix

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
print(mat[1,2])

#extracting sub-matrices
#top-right matrix
print(mat[:2,1:])

#Operations on numpy arrays
#arrays can be added together, or with a scalar 
# all functions can be performed on every element
# refer documentation if needed.
# examples of functions :
# 1. np.sin(arr) 2.np.cos(arr) 3.np.(exp) 4. np.max(arr)