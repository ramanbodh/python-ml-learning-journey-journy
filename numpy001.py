import numpy as np

a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[23,45,3]])
print(b)

a=np.array([a,a*2])
print(a)
print(a.dtype)
print(a.size)
print(a.ndim)

a=np.array([1,2,3],dtype='int32')
print(a)
print(a.dtype)
print(a.size)
print(a.ndim)