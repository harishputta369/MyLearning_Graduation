from array import *

a = array('i', [])
b= array('i',[])
for i in range(4):
    for j in range(2):
        b.append(int(input()))
    a.append(b)
print(a)
for i in range(4):
    for j in range(2):
        print(a[i][j],end=' ')