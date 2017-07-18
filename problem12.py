#!usr/bin/python
triangle=0
divisors=0
i=1
flag=True
while(flag):
	triangle+=i
	print triangle
	for j in range(1,triangle):
		if(triangle%j==0):
			divisors+=1
			if(divisors>500):
				print triangle
				flag=False
				break
	divisors=0
	i+=1
	
	
