# pell number

def pell(n):
    if n<=1:
        return 2
    else:
        return 2*pell(n-1) + pell(n-2)

for i in range(25):
    print(pell(i))