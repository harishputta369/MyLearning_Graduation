
#n=int(input())
#a=list(map(int,input().split()))
#d=int(input('no of rotations'))
def array_left_rotation1(a,n,d):

    for i in range(d):
        temp = a[0]
        lv_templist = []
        for j in range(1,n):
                lv_templist.append(a[j])
        lv_templist.append(temp)
        a = lv_templist
    return a

def array_leftrotation2(a,n,d):
    return a[d:] + a[0:d]

a=[1,2,3,4,5]
n= 5
d =4
print(array_left_rotation1(a,n,d))

print( )

print(array_leftrotation2(a,n,d))