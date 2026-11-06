import numpy as np

#Mathematical operation on the numpy array

# a=np.array([2,23,43])
# print(a*4)
# print(a-4)
# print(a+2)
# print(a/2)
# print(a**2)

# #matrix multiplication using numpy matmul
# a=np.array([[1,2,3],[4,5,6]])
# b=np.full((4,2),6)
# print(a)
# print(b)
# print(np.matmul(b,a))

# #LInear Algebra using numpy
# a=np.array([[1,2,3],[0,5,6],[2,3,4]])
# b=np.identity(5)
# print(a)
# print(b)
# c=np.linalg.det(a)
# print(c)

# #statistic with numpy array

# stat=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.max(stat))
# print(np.max(stat,axis=0))#from each columne 
# print(np.max(stat,axis=1))#from each row 
# print(np.min(stat))
# print(np.min(stat,axis=0))#from each columne 
# print(np.min(stat,axis=1))#from each row 
# print(np.sum(stat))
# print(np.sum(stat,axis=0))#from each columne 
# print(np.sum(stat,axis=1))#from each row 

# reorganining array or reshape 
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.reshape((1,9)))
print(a.reshape((9,1)))