# approximating the value of pi using monte-carlo integration

from random import *
s=c=0
n=0
while True:
    x=random()
    y=random()
    if (x**2+y**2<=1):
        c+=1
    s+=1
    print((c/s)*4)
    n+=1
