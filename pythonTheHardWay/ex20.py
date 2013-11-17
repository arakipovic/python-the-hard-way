from sys import argv

script, filename = argv

def print_all(file) :
	print file.read() 

def rewind(file) :
	file.seek(0)
	
def print_line(cnt, file) :
	print cnt, file.readline()
	

	
in_file = open(filename)
print_all(in_file)
rewind(in_file)
print_line(1, in_file)