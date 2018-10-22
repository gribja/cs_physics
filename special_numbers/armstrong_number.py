# Armstrong numbers

def armstrong(x):
        k = str(x)
        res = 0
        
        for i in range(0,len(k)):
                res += int(k[i])**3

        return (res==x)

print(armstrong(153))
