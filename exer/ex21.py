def add( a, b):
	print" ADDINg %d + %d" %(a, b)
	return a + b

def sub(a, b):
	print " SUBTRACTING %d - %d" %(a, b)
	return a - b
	
def multiply(a, b):
	print " MULTIPLYING %d * %d" %(a, b)
	return a * b
	
def div(a, b):
	print "Dividing %d / %d" %(a, b)
	return a / b
	
print " Lets try enter values differently"

age = add(10, 14)
weight = sub(100, 47)
height = multiply(10, 16)
iq = div(150, 5)

print " Age : %r, weight : %r, height : %r, iq: %r " %(age,weight,height,iq)

print " Solve this"

what = add(age, sub(weight, multiply(height, div(iq, 3))))

print "That become", what, "try that by hand"

