# IGNORE WARNINGS
#--------------------------------
import warnings
warnings.simplefilter("ignore")


# STRING FORMAT
#--------------------------------
# more: https://mkaz.tech/code/python-string-format-cookbook/
print 'this score is {}'.format(1.1234)
'this score is 1.1234'
print 'this score is {:.2f}'.format(1.1234) # 2 decimal format
'this score is 1.12'

# 0 PADDING
test = '1'
test.zfill(5)
'00001'


# NUMBER FORMAT
#--------------------------------
format(MSE, 'e') # convert to 'e' format
>>> 6.769587e+09

# https://docs.python.org/2/library/string.html#formatspec
# different format codes

"{:.2f}".format(14/2) #force 2 decimal places, with rounding off nearest
# 7.00


# SPLITTING
#--------------------------------
import textwrap
textwrap.wrap('ABCDEFG',2)
# ['AB', 'CD', 'EF', 'G']

textwrap.fill('ABCDEFG',2)
# 'AB\nCD\nEF\nG'

import re
re.findall('.{1,2}', '123456789')
# ['12', '34', '56', '78', '9']


# MAP & REDUCE
#--------------------------------
from functools import reduce
reduce(lambda x, y: x*y, [1,2,3,4,5,6])
# 720

map(int, ['1','2','3','4','5','6'])
# [1,2,3,4,5,6]


# ITERTOOLS
#--------------------------------
# all permutations within list
from itertools import permutations
print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

# limit no. in each permutation, without order
list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# permutations but with order
from itertools import combinations
list(combinations([1,2,3], 2))
# [(1, 2), (1, 3), (2, 3)]

# permutations but without order, but allow matching with itself
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2)
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# all permutations between lists
from itertools import product
list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]

B = [[1,2],[3,4],[7,8]]
list(product(*B))
# [(1, 3, 7),
#  (1, 3, 8),
#  (1, 4, 7),
#  (1, 4, 8),
#  (2, 3, 7),
#  (2, 3, 8),
#  (2, 4, 7),
#  (2, 4, 8)]


# groupby; for each unique value, find the number of occurences
from itertools import groupby
s = '1222311'
for a, b in groupby(s):
    print(a, list(b))
# 1 ['1']
# 2 ['2', '2', '2']
# 3 ['3']
# 1 ['1', '1']


# Zipping
A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]


# product: get combinations with repeated factor. useful for brute force, though memory might be an issue if the input is large
from itertools import product
alphalist = 'abcdefghijklmnopqrstuvwxyz'
list(product(alphalist, repeat=2))



# FREQUENCY COUNT
#--------------------------------
from collections import Counter
words = ['this','this','is','a','test']
Counter(words).most_common(3) # top 3 words
# [('this', 2), ('is', 1), ('a', 1)]



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

# can change the start number
for num, i in enumerate(a, 1):
    print num, i

1 10
2 123
3 1231
4 232143434
5 234235

# LIST SLICING
#--------------------------------
list1[-1] # get last in the list
list1[::20] # get every 20th feature
list1[::-1] # reverse sort the entire list
list1[::,0] # for a nested list, grab first value

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

# sort
    # for sorting 2nd position of a tuple within a list
list2 = [(1,2),(53,12),(23,232),(99,231)]
    # reverse is descending order; if only this argument, will take first item of the nested list
    # key is to take position of sort if it is a nested list
sorted(list2, reverse=True, key=lambda x: x[1]) 
# [(23, 232), (99, 231), (53, 12), (1, 2)]

    # sorting asc & dec order in nested list
list2 = [(1, 1), (3, 1), (5, 3), (4, 3)]
sorted(list2, reverse=True, key=lambda x: (x[1], -x[0]))
# [(4, 3), (5, 3), (1, 1), (3, 1)]


# reverse sort
list1 = [1,2,3,4,5]
list1[::-1]
# [5,4,3,2,1]


# DICTIONARY
#--------------------------------
dictname.items()
# dict_items([('97', 63), ('129', 1), ('134', 2)])
dictname.keys()
# dict_keys(['97', '129', '134'])
dictname.values()
# dict_values([63, 1, 2])

# call value using key name
dictname['keyname']

# remove key
dictname.pop('keyName')

# update new values through iteration
newdict = {}
for a, b in values:
    newdict.update({a,b})
# OR
{int(a): b for a,b in values}


# CONCAT
#--------------------------------
s = "-"
seq = ("a", "b", "c")
print (s.join(seq))
# a-b-c


# SORTING
#--------------------------------
sorted(token, reverse=True) # default is ascending, reverse=True is descending
token.reverse() # easier, but it will change the base variable

# there is a key parameter that can select which value in the tuple to be sorted by
sorted(student_tuples, key=lambda x: x[2])
import operator
sorted(btwnCent.items(), key=operator.itemgetter(1), reverse = True)

# JSON
#--------------------------------
sample = {'this': 1, 'this2':3}

import json
with open('result.json', 'w') as fp:
    json.dump(sample,fp)


# RANDOM NUMBER GENERATOR
# ----------------------------
import random
random.uniform(1.5, 1.9) # float
random.randint(0, 5) # integer


# DIVISION IN DECIMALS
#--------------------------------
# in python, there is no decimals if you do a division. Use the following to obtain it.
# only for python 2.7
# fixed in python 3>
4 / float(100)
0.04
4 / 100.0
0.04


# DUPLICATES
#--------------------------------
list1 = ['a', 'a', 'b', 'c', 'd', 'd']
len(list1) # 6
len(set(list1)) # 4
print set(list1) # set(['a', 'c', 'b', 'd'])
print list(set(list1)) # ['a', 'c', 'b', 'd'] #conversion to list takes time

# remove item by value
list1.remove('valuename')
# remove item by index
del list1[0]



a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
# union
a.union(b) # Values which exist in a or b
a|b #OR
# {2, 4, 5, 9, 11, 12}

# intersection
a.intersection(b) # Values which exist in a and b
a&b #OR
# {2, 4}

# difference
a.difference(b) # Values which exist in a but not in b
a-b #OR
# {9, 5}

# symmetrical difference
a.symmetrical_difference(b)
a^b
# {9, 5, 11, 12}


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


import time
# current date
time.strftime("%d/%m/%Y")
# current time in epoch
time.time()

# TIME DELTAS -----
from datetime import datetime, timedelta
print datetime.now()
# 2017-09-05 21:17:02.111204
print datetime.now().date()
# 2017-09-05
print datetime.now() + timedelta(days=5, hours=-5)
# 2017-09-10 16:17:02.419905


import datetime
a = datetime.datetime.now()
b = datetime.datetime.now()
c = b-a
c
# datetime.timedelta(0, 5, 228578) => days, seconds, microseconds
c.days, c.seconds
# (0, 5); days, seconds


# Parsing Time Formats
#----------------------
# dateutil.parser is very good at parsing all times of date formats into standard ones
import dateutil.parser
from datetime import datetime

# note that the default day if not present will be the current day, have to add a manual default to override
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0)).date()
# 2014-02-01

# fuzzy = True ignores any exceptions
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0), fuzzy=True).date()

# extracting date parts & time delta
t1='Sun 10 May 2015 13:54:36 -0700' #with timezone
t2='Sun 10 May 2015 13:54:37 -0000'
x = dateutil.parser.parse(t1)
y = dateutil.parser.parse(t2)
print(x.year,x.month,x.day,x.hour,x.minute,x.second)
# 2015 5 10 13 54 36
z=y-x
print(z)
# 7:00:00
print(z.days,z.seconds,z.microseconds)
# 0 420 0
print(z.total_seconds())
# 420




# get day of week
import datetime
print(datetime.datetime.strptime(input(), '%m %d %Y').strftime('%A').upper())
# OR
from calendar import weekday, day_name
day_name[weekday(year,month,day)].upper()


# Set Timezone to Local
#----------------------
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
        # "C:\Users\xx\xx\Scripts\MyPythonScripts\facebook_public.py"
  # Note that double quotes needed is there are spaces in path



# EXCEPTION HANDLING
#--------------------------------
import sys
import traceback

try:
    something
except Exception as e:
    print(sys.exc_info()[2].tb_lineno) # line number where code breaks
    print(e) # exact item that have issue
    print(traceback.format_exc()) # full traceback error


# using raise to effect an exception
try:
    if line1 != line2:
        raise Exception('Stations are not in the same line')
except Exception as e:
    print(e)

# SUBPROCESS
#--------------------------------
# call command prompt in python

import subprocess

subprocess.call(r"""mongoexport --db test-database --collection wsg --type=csv --fieldFile "C:\Users\Teo S\Desktop\fields.txt"
                    --out export.csv""", shell=True)
subprocess.call(["mongoexport", "--db", "test-database", "--collection", "wsg", "--type=csv", "--fieldFile", "fields.txt" ,
                    "--out", "export.csv"])
                    
# output value of 1 means good

# open a file
import subprocess
import os

path_to_notepad = r'C:\Windows\System32\notepad.exe'
path_to_file = r'C:\Users\Desktop\hello.txt'

subprocess.call([path_to_notepad, path_to_file]) #note the list brackets


# Virtual Environment
#--------------------------------
# https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

virtualenv env # create a virtual env called env
source env/bin/activate # change python env to work within env
which python # confirm python env is in virtual
deactivate # escape from virtual env


# Local Server
#--------------------------------
python -m SimpleHTTPServer 3000 # python2
python -m http.server 3000 # python3


# PRETTY PRINTS
#--------------------------------

# pretty print json, dictionary etc.
from pprint import pprint
pprint(the_list)


# print a table
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["name", "rank", "gender"]
table.append_row(["Jacob", 1, "boy"])
table.append_row(["Isabella", 1, "girl"])
table.append_row(["Ethan", 2, "boy"])
table.append_row(["Sophia", 2, "girl"])
table.append_row(["Michael", 3, "boy"])
print(table)

+----------+------+--------+
|   name   | rank | gender |
+----------+------+--------+
|  Jacob   |  1   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
|  Ethan   |  2   |  boy   |
+----------+------+--------+
|  Sophia  |  2   |  girl  |
+----------+------+--------+
| Michael  |  3   |  boy   |
+----------+------+--------+


# pretty print json
import json

your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
parsed = json.loads(your_json)
print json.dumps(parsed, indent=4, sort_keys=True)


# PDF -------------------------
# convert list of images into PDF
from fpdf import FPDF
import os

# get list of images file path
path = r'/Users/xx/Desktop/foldername'
[path+'/'+i for i in os.listdir(path)]

pdf = FPDF() # use FPDF('L') for landscape
x,y,w,h = 0,0,200,300 # dimensions for A4, might need to adjust accordingly
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")



# reduce pdf report to just specific pages
from PyPDF2 import PdfFileWriter, PdfFileReader
file = 'report.pdf'

inputpdf = PdfFileReader(open(file, "rb"))
output = PdfFileWriter()

for i in range(inputpdf.numPages):
    if i >= 8 and i <= 28: # retain pages from 9 to 29
        p = inputpdf.getPage(i)
        output.addPage(p)

with open('greenery.pdf', 'wb') as f:
    output.write(f)


# PYAUTOGUI -------------------------
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# get coordinates
print(pyautogui.position())
# click
pyautogui.click(coordinates)
# single key
pyautogui.press('enter')
# consecutive keys
pyautogui.hotkey('ctrl', ‘f4’)



# ENVIRONMENT VARIABLES -------------------------
# e.g.
if len(sys.argv) == 1: # ensure a variable is entered
    print('Please provide a valid IP address\n')
    sys.exit()
webcam_ip = str(sys.argv[1])
# in cmd
python main.py 192.168.5.111
