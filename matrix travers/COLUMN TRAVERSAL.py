a = []
for i in range(5):
    row = [int(i) for i in input().split()]
    a.append(row)
print(a)
n = len(row)  # len(a[0])
for i in range(n):
    for j in a: # matrix lo first element is nothing but rows
        print(j[i], end=' ')
    print('||')