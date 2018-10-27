# demlo number

def demlo(x):
    k = str(x)
    n = len(k)
    res = ""

    for i in range(1,n+1):
        res += str(i)

    for i in reversed(range(1,n)):
        res += str(i)

    return res

print(demlo(1111))
