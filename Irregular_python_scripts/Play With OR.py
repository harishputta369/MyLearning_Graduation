def orofarray(arr,N):
    for i in range(N-1):
        arr[i]=arr[i]|arr[i+1]
    return arr
#print(orofarray([10, 11, 1, 2, 3],5))
#print(orofarray([5,9,2,6],4))
