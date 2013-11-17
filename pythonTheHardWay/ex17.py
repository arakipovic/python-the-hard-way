from sys import argv
from os.path import exists

script, fin, fout = argv
ff = open(fin)
fdata = ff.read()

print exists(fout)
foutf = open(fout, "w")
foutf.write(fdata)

ff.close()
foutf.close()