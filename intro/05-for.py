# iteration over list
people = ["william", "peter", "stephen", "nicolas"]

for someone in people:
    print someone


# iteration over dict
william = { "first_name": "William", "last_name": "Mayer", "Age": 40 }

for k, v in william.iteritems(): # Just only items() in python 3
    print "%s: %s" % (k, v)

# iteration over range
numbers = range(0, 10)

for i in numbers:
    print "The current postion is %d" % i
