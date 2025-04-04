def Maxofsubarray(arr,n):
    x=1
    for i in range(n-1):
        x=max(x,arr[i]^arr[i+1])
    return x
#print(Maxofsubarray([1,2,3,4],4))