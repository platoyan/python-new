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
print(type(np.array([6,7,8])))

#Array Creation:
#There are several ways to create arrays:
a=np.array([2,3,4])
#a=np.array(2,3,4) #WRONG
#array transforms sequences of sequences into two-dimensional arrays
#array transforms sequences of sequences of sequences into three-dimensional arrays
b=np.array([(1,2,4),(5,6,7)])
print(b)

c=np.array([[1,3],[5,6]],dtype=complex)
print(c)

#The function zeros creates an array full of zeros
z=np.zeros((3,5))
print('----------')
print(z) 
#The function ones creates an array full of ones
o=np.ones((3,5,2),dtype=np.int32)
print('----------')
print(o)
#The function empty creates an array whose initial content is random and depends on the state of the memory.
e=np.empty((2,3))
print('----------')
print(e)