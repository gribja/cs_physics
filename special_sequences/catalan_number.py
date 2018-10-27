# catalan number

# a function to determine the factorial of a given number

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f*=i
    return f


# a function for n_chooses_r

def n_c_r(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

# first 25 of these numbers

k = 0
while k<=25:
    p = n_c_r(2*k,k)/(k+1)
    c = factorial(2*k)/(factorial(k)*factorial(k+1))
    print(p)
    k += 1