# newton raphson method for finding root of an equation efficiently

def f(x):
    return x**3-2*x-5

def derive(func,a):
    h=1e-15
    s=func(a+h)-func(a)
    return float(s)/h

def newton_raphson(x):
    c = x
    n = 4

    for i in range(n):
    	k = c - (f(c)/derive(f,c))
    	c = k
    return k

print(newton_raphson(2))