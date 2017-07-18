#!usr/bin/python
def ps(dimensions):
	paths=1
	for i in xrange(1, dimensions+1): 
		paths=paths*i
	return paths

print ps(40)/ps(20)/ps(20)
