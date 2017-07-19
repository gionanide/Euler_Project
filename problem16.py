#!usr/bin/python
number=2**1000
numberLen=str(number)
sum=0
for i in range(len(numberLen)):
	sum+=int(numberLen[i])
print sum

