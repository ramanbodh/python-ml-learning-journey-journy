import numpy as np

#here we are going to initialised different np arrays using different np methodes

a=np.zeros((3,3),dtype="int32")
print(a)

b=np.ones((3,3),dtype="int32")
print(b)
print(b.dtype)
print(b.itemsize)
print(b.size)
print(b.shape)

c=np.full((2,3),7,dtype="int16")
print(c)

# initialising the matrix using np of like 
# [[1,1,1,1,1]
#  [1,0,0,0,1]
#  [1,0,7,0,1]
#  [1,0,0,0,1]
#  [1,1,1,1,1]]

outer=np.ones((5,5))
inner=np.zeros((3,3))
inner[1,1]=7
output=outer.copy()
output[1:-1,1:-1]=inner
print(outer)
print(inner)
print(output)