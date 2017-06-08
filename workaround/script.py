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


from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year,now.hour, now.minute, now.second)


#----------------------------------------------------

#to print 2 places after decimal
print("%.2f" % total)

#----------------------------------------------------
#sample loop

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()
#----------------------------------------------------
#sample datetime manipulations
import datetime

start()

def start():
	ist_time = datetime.datetime.now()
	
	et_time = ist_time - datetime.timedelta(hours=9)
	
	#reduce the number of hours, first parameter is days and the next is seconds
	uk_time = ist_time - datetime.timedelta(0, 32400)
	print "IST time: %s" %(ist_time)
	print "ET time: %s" %(et_time)
	print "UK time: %s" %(uk_time)

