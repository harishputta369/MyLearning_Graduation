def outputarray(arr,N):

#def op(arr,N):
    for i in range(N-1):
        arr[i]=arr[i]^arr[i+1]
    return arr
print(outputarray([10, 11, 1, 2, 3],5))
#print((op([10,11,1,2,3],5)))