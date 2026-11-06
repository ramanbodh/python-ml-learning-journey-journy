import numpy as np

# #random initialisation of np arrays elements

# #random decimal number between 0 to 1
# a=np.random.rand(2)
# print(a)
# a=np.random.rand(3,2)
# print(a)

# #random integer
# a=np.random.randint(2,9,size=(3,3))
# print(a)
# b=np.random.random_sample(a.size)
# print(b)

# b=np.random.random_sample(size=(3,2))#it arguments says size but it takes the shape of sample 
# print(b)

a=np.identity(5)
print(a)

a=np.array([1,2,3])
print(a)
b=np.repeat(a,3)
print(b)
c=np.array([a])#now is matrix before it was vector, so now it have axis also
b=np.repeat(c,3)#by default axis is 1 
print(b)
b=np.repeat(c,3,axis=0)#for rows 
print(b)



