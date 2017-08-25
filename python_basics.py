# STRING FORMAT
#--------------------------------
# more: https://mkaz.tech/code/python-string-format-cookbook/
print 'this score is {}'.format(1.1234)
>>> 'this score is 1.1234'
print 'this score is {:.2f}'.format(1.1234) # 2 decimal format
>>> 'this score is 1.12'



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


# dateutil.parser is very good at parsing all times of date formats into standard ones
import dateutil.parser
from datetime import datetime

# note that the default day if not present will be the current day, have to add a manual default to override
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0)).date()
# 2014-02-01

# fuzzy = True ignores any exceptions
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0), fuzzy=True).date()
