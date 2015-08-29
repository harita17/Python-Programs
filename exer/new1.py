def sweets (booking):
    ladoos = booking * 650
    jilebies = ladoos + 1500
    kachories = jilebies / 500
    return ladoos, jilebies, kachories


total = 15000

ladoos, jilebies, kachories = sweets(total)

print "With a starting point of: %d" % total
print "We'd have %d ladoos, %d jilebies, and %d kachories." % (ladoos, jilebies, kachories)
