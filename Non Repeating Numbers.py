def Non_Repeating_Numbers(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]==arr[j]):
                arr[i]=0
                arr[j]=0
    arr.sort()
    return [arr[-2],arr[-1]]
print(Non_Repeating_Numbers([1, 2, 3, 2, 1, 4]))
print(Non_Repeating_Numbers([2, 1, 3, 2]))
def reg(arr):
    a=[]
    for i in range(len(arr)):
        if (arr.count(arr[i])==1):
            a.append(arr[i])
    return a
print(reg([1, 2, 3, 2, 1, 4]))
print(reg([2, 1, 3, 2]))