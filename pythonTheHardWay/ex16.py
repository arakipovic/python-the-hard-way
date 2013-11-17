from sys import argv

script, filename = argv

file = open(filename, "w")
file.truncate();

file.write("linija\n")
file.write("linija\n")

file.close()