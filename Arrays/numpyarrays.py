import numpy as np
a=np.array([1,3,5,7])
print(a)
b=np.array([[1,2,3],[4,5,6],[7,8,9],[0,0,0]])
print(b)
print(b.size)
print(b.shape)
i,j=b.shape[0],b.shape[1]
print(i)
print(j)
for x in range(i):
    for y in range(j):
        print(b[x][y],end=' ')
    print()