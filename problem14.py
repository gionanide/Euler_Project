#!usr/bin/python
maxChain=-10
for Startingnumber in range(1,1000001):	
	chain=0
	while(not(Startingnumber==1)):
		if(Startingnumber%2==0):
			Startingnumber=Startingnumber/2
		elif(Startingnumber%2==1):
			Startingnumber=3*Startingnumber+1
		chain+=1
	print chain
	if(chain>maxChain):
		maxNumber=Startingnumber
print maxNumber

