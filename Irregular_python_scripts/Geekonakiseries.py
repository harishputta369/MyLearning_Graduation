def add_three_numbers(a,b,c):
    return a+b+c
def find_Nth_number(A,B,C,N):
    arr=[A,B,C]
    #adding numbers to array
    for i in range(3,N):
        arr.append(add_three_numbers(arr[i-1],arr[i-2],arr[i-3]))
    return arr[-1]
for x in range(int(input())):
    Arr=list(map(int,input().split()))
    a,b,c,n = Arr[0],Arr[1],Arr[2],Arr[3]
    print(find_Nth_number(a,b,c,n))