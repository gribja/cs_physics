# Trapezoidal Rule for numerical Integration
def f(x):
	return x**4-2*x+1

def int(func,a,b):
	n = 10000000000
	h = (b-a)/n
	s = (1/2)*(func(a)+func(b))
	
	for i in range(1,n):
		s += func(a+i*h)
	return h*s


print(int(f,0,2))
