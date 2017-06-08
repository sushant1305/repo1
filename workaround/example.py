import datetime

start()

def start():
	ist_time = datetime.datetime.now()
	et_time = ist_time - datetime.timedelta(hours=9)
	uk_time = ist_time - datetime.timedelta(0, 32400)
	print "IST time: %s" %(ist_time)
	print "ET time: %s" %(et_time)
	print "UK time: %s" %(uk_time)


