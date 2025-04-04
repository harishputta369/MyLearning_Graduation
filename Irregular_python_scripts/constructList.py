def constructList(N,Q):
    arr=[0]
    for i in range(N):
        #print(arr)
        if (Q[i][0]==0):
            arr.append(Q[i][1])
        else:
            for j in range(len(arr)):
                arr[j]=arr[j]^Q[i][1]
                #print(Q[i][1])
    arr.sort()
    return arr
print(constructList(3,[[0,2],[1,3],[0,5]]))