import numpy as np

# accessing & changing the each element of the numpy array

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.size)

#getting specific element like 13
print(a[1,5])
#another way to the same result negative indexing 
print(a[1,-2])

#getting specific column 
print(a[:,2])
#same with use of negative indexing
print(a[:,-5])

#getting specific row
print(a[0])

#more fancy way of getting the elements (starting index:ending index: step value)
print(a[:,1:6:2])
#same result 
print(a[:,1:-1:2])
