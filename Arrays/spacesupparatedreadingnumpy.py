from numpy import *
import array as A
a=A.array('i',map(int,input().split()))
b=array([])
for i in range(4):
    b=append(b,[a])
print(b)
print(b.shape)

# we cannot use both arrays numpy and regular arrays at time in an efficient manner
