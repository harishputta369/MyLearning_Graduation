from numpy import *
a=array([])
b=array([])
for i in range(5):
    for j in range(5):
        a=append(a,1)
    b=append(b,list(list(a)))
print(b)
print(b.shape)
print(a)