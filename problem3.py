#!usr/bin/python
number = 600851475143
largestFact = 0
 
for i in range(2,number):
	if (number%i==0):
		isPrime = True
		for j in range(2,i):
            		if(i%j==0):
                		isPrime = False
                		break
        	if (isPrime):
            		largestFact=i
