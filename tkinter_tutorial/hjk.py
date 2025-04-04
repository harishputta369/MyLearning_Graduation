input1=8
input2=[44,45,56,39,2,6,17,75]
input3=1
input4=[54]
def maxPairs(input1,input2,input3,input4):
    c=0
    for i in range(input3):
        for j in range(input1):
            if input4[i]>=input2[j]:
                c+=1
    return c
print(maxPairs(input1,input2,input3,input4))