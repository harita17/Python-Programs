def harita (arg1, arg2):
	print "arg1 : %r, arg2 : %r " % (arg1, arg2)

def goutham (*args):
	arg1, arg2 = args
	print "arg1 : %r, arg2 : %r " % (arg1, arg2)

def mom(arg1):
	print "arg1: %r" % arg1

def none():
	print " i hav none "

harita("Good", " girl")
goutham("Bad", "boy" )
mom(" great mom")
none()
