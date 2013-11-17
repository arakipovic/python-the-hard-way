from sys import argv

script, filename = argv

txt = open(filename)
print "file %r" % txt
print txt.read()