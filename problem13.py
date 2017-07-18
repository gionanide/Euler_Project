#!usr/bin/python
sum=0
with open('/home/manos/number','r') as file:
	for line in file.readlines():
		i=int(line)
		sum+=i	
sum1=str(sum)
print(sum1[:10])

