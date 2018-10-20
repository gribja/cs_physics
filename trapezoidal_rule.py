# Trapezoidal Rule for numerical Integration
def f(x):
	return x**4-5*x**3+7

def int(func,a,b):
	n = 100000
	h = (b-a)/n
	s = (1/2)*(func(a)+func(b))
	
	for i in range(1,n):
		s += func(a+i*h)
	return h*s


print(int(f,5,10))
