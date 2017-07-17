#!usr/bin/python
sum=0
n=2000000
for p in range(2, n+1):
	for i in range(2, p):
        	if p % i == 0:
            		break
    	else:
        	sum+=p
print sum

