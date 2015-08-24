from sys import argv
from os.path import exists

script, from_file, to_file = argv

print " we are coping data from %s to %s " % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "the length of the file is %d BYTES" % len(indata)
print "does the output file exist %r" % exists(to_file)

print "Hit RETURN to cntinue and CRTL C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)


print " ALL DONE "

out_file.close()
in_file.close()

