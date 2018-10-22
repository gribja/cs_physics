# finding a root of a given equation by applying bisection method

def f(x):
    return x**3-2*x+1

def bisect(func,a,b):
    if (func(a)*func(b) >= 0):
        print("you have not assumed the right a and b")
        return
    else:
        c = a
        while ((b-a)>=0.01):
            c = (a+b)/2
            if c!=0:
                if (func(a)*func(c)<0):
                    b = c
                elif (func(b)*func(c)<0):
                    a = c
                else:
                    print("given funtion doesn't follow necessary assumptions")
            else:
                break
    return c

print(bisect(f,-200,300))  
