#https://docs.scipy.org/doc/numpy/user/quickstart.html#the-basics
#NumPy's array class is called ndarray
import numpy as np
#arange([start, ]stop, [step, ]dtype=None)
a = np.arange(15).reshape(3,5)
print(a)
print(a.shape) #the dimensions of the array
print(a.ndim) #the number of axes (dimensions) of the array. 
print(a.dtype.name) #an object describing the type of the elements in the array. int32
print(a.itemsize) #the size in bytes of each element of the array.
print(a.size) #the total number of elements of the array 
print(np.array([6,7,8]))
