def print_two(*args) : 
	arg1, arg2 = args
	print "%r, %r" % (arg1, arg2)
	
def print_two(arg1, arg2) : 
	print "%r, %r" % (arg1, arg2)

def print_one(arg1) : 
	print "%r" % (arg1)
	
def print_none() :
	print "nema"
	
	
print_two("prvi", 2)
print_two(1, 2)
print_one(4)
print_none()