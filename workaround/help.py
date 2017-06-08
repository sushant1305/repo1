#Sample Python Program

#""""Multiline Comment
#aabbbbbbbbdbbdd
#bdfbdfb""""

#Methods that use dot notation only work with strings.
#On the other hand, len() and str() can work on other data types.



a = 10 ** 2
b = "SUSHANT"[4]
c = "United States of America"

num_to_str = 3.145

print a
print b
print len(c)
print c.lower()
print c.upper()

print str(num_to_str)
print "United " + "Arab " + "Emirates"
print "The value of pi is around " + str(3.14)

#Print a variable value with string
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#name = raw_input("Enter your name:")

#print "Hi %s"% (name)
#---------------------------------------------------
#using datetime

from datetime import datetime

print datetime.now()

now = datetime.now()
print now
print now.year
print now.month
print now.day
#print date in desired format
print '%s-%s-%s' % (now.year, now.month, now.day)

#print time in desired format
print '%s:%s:%s' % (now.hour, now.minute, now.second)


#----------------------------------------------------
