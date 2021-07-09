#Introduction to Numpy module and Numpy Arrays

#Numpy is a scientific library that deals with array objects.
#It includes operations on arrays which are 
#1. Mathematical 2. Logical 3. Manipulation of shape 
#4.Statistical operations 5. Random simulations.


#Numpy module has two powerful operations : 
#1. Broadcasting -> same operation for numbers, objects and arrays.
#2. Vectorization -> no complex for loops 

#In numpy , dimensions are called AXES.


# ---- IMPORTING NUMPY MODULE ----

import numpy as np

# ---- CREATING A NUMPY ARRAY ---- 

my_list = [1,2,3,4,5]
my_arr = np.array(my_list)
print(my_arr)

my_arr2 = np.arange(10)
print(my_arr2)

my_arr3 = np.arange(1,11,2)
print(my_arr3)

my_arr4 = np.random.rand(5)
print(my_arr4)

my_arr5 = np.random.randn(2)
print(my_arr5)

my_arr6 = np.random.randn(2,2)
print(my_arr6)

#creating matrix with zero elements 

my_arr7 = np.zeros((3,3))
print(my_arr7)

#creating an identity matrix
my_arr8 = np.eye(5)
print(my_arr8)

#using linspace

my_arr9 = np.linspace(0,1,99)
print(my_arr9)

#Some basic numpy methods

my_arr10 = my_arr2.reshape(2,5)
print(my_arr10)

print(my_arr9.max())

print(my_arr9.min())

print("index of max value is :", my_arr9.argmax())

print("index of min value is : ", my_arr9.argmin())

print("data type of array 9 is : ",my_arr9.dtype)

print(type(my_arr9))

#size,shape and ndim are other methods in numpy




