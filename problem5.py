#!usr/bin/python
def devides(number):
	for dividor in range(1, 21):
        	if((number%dividor)!= 0):
            		return False
    	return True

counter = 2520
while True:
	print counter
    	if devides(counter):
        	print counter
        	break
	counter +=20

