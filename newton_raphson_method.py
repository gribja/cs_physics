# newton raphson method for finding root of an equation efficiently

def f(x):
    return x**3-2*x+1

def derive(func,a):
    h=1e-15
    s=func(a+h)-func(a)
    return float(s)/h

def newton_raphson(x,p):
    c = p
    k = x - (f(x)/derive(f,x))
    n = 5

    for i in range(n):
        c = k
    return c

print(newton_raphson(5,1))
