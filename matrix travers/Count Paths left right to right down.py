def count(row,col):
    if row == 1 or col ==1:
        return 1
    return (count(row-1,col)+count(row,col-1)) # this returns no of splits happend by the function
print(count(6,6))
'''''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(row+col)//fact(row)+fact(col))
'''''