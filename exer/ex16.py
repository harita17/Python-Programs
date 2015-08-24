from sys import argv

script, filename = argv

print "we are going to erase the file %r " % filename
print " if you dont wat to continu click CTRL C [^C] "
print " If you do want to continue press RETURN"

raw_input("?")

print " Opening the file"
target = open(filename, 'w')

print " Im truncating the file "
target.truncate()

print " now please enter 3 lines as asked bellow"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print " im going to writ these line toa  file "

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and we are closing the file"
target.close()

