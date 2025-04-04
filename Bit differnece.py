def bitdifsingle(x,y):
    a=x^y #tells diffrence bits gets 1ns
    count = 0
    while (a!=0):
        if a&1 == 1:
            count+=1
        a=a>>1
    return count
def Bitdiffrence(arr):
    countarr=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            countarr.append(bitdifsingle(arr[i],arr[j]))
    return sum(countarr)
#print(Bitdiffrence([1,3,5]))
#print(Bitdiffrence([2, 4]))
#print(bitdifsingle(2,7))