#!usr/bin/python
sum=0
a1=0
a2=1
a3=a1+a2
while(a3<4000000):
	if(a3%2==0):
		sum+=a3
	a1=a2
	a2=a3
	a3=a1+a2
print sum
