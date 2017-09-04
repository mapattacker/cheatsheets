# STRING FORMAT
#--------------------------------
# more: https://mkaz.tech/code/python-string-format-cookbook/
print 'this score is {}'.format(1.1234)
>>> 'this score is 1.1234'
print 'this score is {:.2f}'.format(1.1234) # 2 decimal format
>>> 'this score is 1.12'


# LOOPS
#--------------------------------
# enumerate
a = [10,123,1231,232143434,234235]
for num, i in enumerate(a):
    print num, i

0 10
1 123
2 1231
3 232143434
4 234235


# LIST SLICING
#--------------------------------
list1[-1] # get last in the list
list1[::20] # get every 20th feature

# append
x = [1, 2, 3]
x.append([4, 5])
print (x)
>>>[1, 2, 3, [4, 5]]

# extend
x = [1, 2, 3]
x.extend([4, 5])
print (x)
>>>[1, 2, 3, 4, 5]


# SORTING
#--------------------------------
sorted(token, reverse=True) # default is ascending, reverse=True is descending


# DIVISION IN DECIMALS
#--------------------------------
# in python, there is no decimals if you do a division. Use the following to obtain it.
# only for python 2.7
# fixed in python 3>
>>> 4 / float(100)
0.04
>>> 4 / 100.0
0.04


# DUPLICATES
#--------------------------------
list1 = ['a', 'a', 'b', 'c', 'd', 'd']
len(list1) # 6
len(set(list1)) # 4
print set(list1) # set(['a', 'c', 'b', 'd'])


# PICKLING
#--------------------------------
# http://www.pitt.edu/~naraehan/python2/pickling.html
# saving your Python data object as itself
# also see https://stackoverflow.com/questions/26860051/how-to-reduce-the-time-taken-to-load-a-pickle-file-in-python
import cPickle

f = open('gradesdict.p', 'rb')
mydict = cPickle.load(f)       
f.close()


# READING FROM ZIP FILE
#--------------------------------



# DATE
#--------------------------------
from datetime import datetime

x = datetime.strptime('2011-01-03', '%Y-%m-%d')
print x
# 2011-01-03 00:00:00
x = datetime.strptime('2011-01-03', '%Y-%m-%d').date()
print x
# 2011-01-03
x = datetime.strptime('2011', '%Y').date()
print x
# 2011-01-01
d = datetime.strptime("22:30", "%H:%M")
print d.strftime("%I:%M %p")
# '10:30 PM'


# dateutil.parser is very good at parsing all times of date formats into standard ones
import dateutil.parser
from datetime import datetime

# note that the default day if not present will be the current day, have to add a manual default to override
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0)).date()
# 2014-02-01

# fuzzy = True ignores any exceptions
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0), fuzzy=True).date()


# Set Timezone to Local
from dateutil import tz

# utc = datetime.utcnow()
utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since 
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=tz.tzutc())
# Convert time zone
central = utc.astimezone(tz.tzlocal())



# TASK SCHEDULER
#--------------------------------
# Go to Task Scheduler
# Create Task
# Give a name
# Under Triggers > Add New > Check Repeat Task > Every 1 Hour or Others > for duration of: Change Indefinitely
# Under Actions > Start a program 
  # > Program/Script (choose python.exe path)
        # C:\ProgramData\Anaconda2\python.exe
  # > Add arguements (choose python script path)
        # "C:\Users\Teo Siyang\Dropbox\Scripts\MyPythonScripts\Social Media\facebook\facebook_public.py"
  # Note that double quotes needed is there are spaces in path


# EXCEPTION HANDLING
#--------------------------------
import sys
import traceback

try:
    something
except Exception, e:
    print sys.exc_info()[2].tb_lineno # line number where code breaks
    print e # exact item that have issue
    print traceback.format_exc() # full traceback error
