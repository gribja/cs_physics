#derivate of given function

def f(x):
    return x**4+5*x**3-6

def derive(func,a):
    h=1e-7
    s=func(a+h)-func(a)
    return float(s)/h

print(derive(f,5))
