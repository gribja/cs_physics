# Sieve of Eratosthenes
# An algorithm for generating prime numbers

def SieveOfEratosthenes(n):
	a = [True for _ in range(n+1)]
	
	p = 2
	
	while (p*p<=n):
		if a[p]==True:
			for j in range(p*2,n+1,p):
				a[j] = False
		p+=1
	
	ar = []
	
	for i in range(2,n):
		if a[i]==True:
			ar.append(i)
	return ar

print(SieveOfEratosthenes(100))