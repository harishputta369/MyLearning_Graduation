def bitsum(a,b):
    while (b!=0):
        sum = a^b
        carry = (a & b)<<1
        a = sum
        b = carry
    return sum
print(bitsum(10,5))