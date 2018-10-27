# krishnamurthy number

from math import factorial as f

def krishnamurthy(x):
    k = str(x)
    res = 0

    for i in range(0,len(k)):
        res += f(int(k[i]))

    return (res==x)

print(krishnamurthy(145))
        
