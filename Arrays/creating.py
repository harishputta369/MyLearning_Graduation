import array as A
a=A.array('i',[1,2,5,6,9])
print('size/len of array is ',a.__sizeof__(),len(a))
for j in range(len(a)):
    print(a[j])

print('-----------------')
alist=[1,2,5,6,9]
for i in range(len(alist)):
    print(alist[i])
print('size len of list is',alist.__sizeof__(),len(alist))
print('-----------------')
