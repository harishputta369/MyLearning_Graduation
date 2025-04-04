def singleElement(N,arr):
    for i in range(N):
        if (arr.count(arr[i])==1):
            return arr[i]
            break
print(singleElement(4,[1,10,1,1]))
