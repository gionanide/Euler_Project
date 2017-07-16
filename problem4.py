#!usr/bin/python
max=-1
for a1 in xrange(1000,0,-1):
	for a2 in xrange(1000,0,-1):
		a3=a1*a2
		numberDigits = str(a3)
		if(len(numberDigits)%2==0):
			firstDigits=numberDigits[:len(numberDigits)/2]
			lastDigits=numberDigits[len(numberDigits)/2:]
			lastDigits=lastDigits[::-1]
			if(firstDigits==lastDigits):
				if(a3>max):
					max=a3
				
		else:
			firstDigits=numberDigits[:len(numberDigits)/2-1/2]
			lastDigits=numberDigits[len(numberDigits)/2+3/2:]
			lastDigits=lastDigits[::-1]
			if(firstDigits==lastDigits):
				if(a3>max):
					max=a3
print max
