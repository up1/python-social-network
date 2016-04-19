# %s for string
message = "World"
print "Hello %s" % message


# %d for numeric and floating point
a = 100
b = 20

print "The value of a is %d" % a
print "The value of b is %d" % b

print "Change value of b to 100"
b = 100
print "The current value of b is %d" % b


# %r for boolean
print "Is a equal to b: %r" % (a == b)


# Mix it
print "\n"
print "Hello %s.\nNow the value of a is %d and the value of b is %d.\nAnd a is equal to b is %r" % (message, a, b, a == b)
