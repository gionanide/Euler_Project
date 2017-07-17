#!usr/bin/python
n=1000000
not_prime = set()
primes = []
for i in range(2, n+1): 
	if i not in not_prime:
        	primes.append(i) 
        	for j in range(i*i, n+1, i): 
                	not_prime.add(j)

print primes[10000]

