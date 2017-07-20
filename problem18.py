#!usr/bin/python
pyramid = [[] for i in range(15)]
z=0
y=2
x=0
with open('/home/manos/number','r') as file:
	for line in file.readlines():	
		for i in range((len(line)-1)/2):
			pyramid[x].append(line[z:y])
			z+=2
			y+=2
		x+=1
		z=0
		y=2
sum=int(pyramid[0][0])
print sum
startingPosition=0
for i in range(1,len(pyramid)):
		if(pyramid[i][startingPosition]>pyramid[i][startingPosition+1]):
			sum+=int(pyramid[i][startingPosition])
		else:
			sum+=int(pyramid[i][startingPosition+1])
			startingPosition=startingPosition+1
print sum
	
	
	
			
	


		

		
