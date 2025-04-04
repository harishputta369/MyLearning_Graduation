import numpy as np
a=np.array([1,2,5,6,9])
print(a.size,a.__sizeof__(),len(a))
for i in a:
    print(i)