import re

# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.regextester.com/15

  # .     (dot) matches any character.
  # *     Matches 0 or more occurrence of preceding expression.
  # +     Matches 1 or more occurrence of preceding expression.
  # ?     Matches 0 or 1 occurences of preceding expression.
  # {n}   Matches exactly n reptitions
  # {n,}  At least n times
  # {,n}  At most n times
  # {m,n} At least m and at most n repetitions (e.g., \d{1,3} means get 1, 2 or 3 digits)
  # ^     Match first character in line
  # $     Match last character of string
  # []    Matches any charcters in the square brackets
  # ()    Groups regular expressions and remembers matched text / output & find only characters in brackets.
  # (?:)  Outputs not just within brackets, but the entire string
  # (?=)  Lookahead. Will assert but not consumed
  # a|b	  Matches either a or b.
  
  # \     backslash changes search code into real symbol (eg., \$)
  
  # [^A-Z]                  does not match alphabets A to Z (^ means does not)
  # ^((?!main-branch).)*$   does not contain the string main-branch
  
  # \b    Word boundary. Matches r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
  # \B    Matches r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'.
  # \w	  Matches word characters (numbers & alphabets). Includes underscore
  # \W	  Matches nonword characters.
  # \d	  Matches digits. Equivalent to [0-9].
  # \D	  Matches nondigits. [^0-9]
  # \s    Matches whitespace
  # \S    Matches non-whitespace

#-------------------------------------------
dir(re) #give list of constantsx
result = re.findall(r'this', email, re.IGNORECASE) #e.g., IGNORECASE ignores casing
result = re.findall(r'this', email, flags=re.I) #alternative



#-------------------------------------------
phone = "2004-959-559 # This is Phone Number"
email = 'this is an bah bah email nick19a@gmail.com the end foo@gmail.com.'


#-------------------------------------------
# match; output if result at start of string
# Unmatched objects return None
num = re.match(r'\w\w\w', phone)
print num.group() #output '200'



#-------------------------------------------
# search; output first result in string
# Unmatched objects return None
# can use s.split(' ') to split the text into individuals words first
num = re.search(r'...4', phone)
print num.group() #output '2004'

num = re.search(r'\sThis', phone)
print num.group() #output ' This'

num = re.search(r'.+559', phone)
print num.group() #output '2004-959-559'

result = re.search(r'\w+@[\w.]+', email)  #find all word characters and dot after @
print result.group()  #output 'nick19a@gmail.com'

# multiple matches, use () in re, and result.groups()
result = re.search(r'(\w+)@([\w.]+)', email)  #split the username & host name using round brackets
print result.groups()  #output ('nick19a', 'gmail.com')
print result.group()  #output 'nick19a@gmail.com'
print result.group(0)  #output 'nick19a@gmail.com'
print result.group(1)  #output 'nick19a'
print result.group(2)  #output 'gmail.com'


#-------------------------------------------
# findall; output all results in a list
num = re.findall(r'2004|Phone', phone)
print num #output ['2004', 'Phone']

result = re.findall(r'(\w+)@([\w.]+)', email)  #find all word characters and dot after @
print result #ouput [('nick19a', 'gmail.com'), ('foo', 'gmail.com.')]

# replace
num = re.sub(r'\W', '', phone)  #3 arguments
print num
re.sub(r'[a-zA-Z]','', string) #remove all alphabets in a string

# insert
s = "x01777"
m = re.sub(r'(\w\d\d)(\d\d\d)', r'\1-\2', s) #\1 \2 indicates the brackets
print(m)
'x01-777'

# split results equally
re.findall('.{1,2}', '123456789')
# ['12', '34', '56', '78', '9']

str = '100,000,000.000'
re.split(r'[,.]')
# ['100', '000', '000', '000']


#-------------------------------------------
# Conditional Split
text = "Perennials. Stolons slender. Perianth bristles 6 or 7, ca. 2 × as long as nutlet"

result = re.split(r'\.\s(?=[A-Z])', text) #(?=somthing) will not remove the something when splitting
['Perennials',
 'Stolons slender',
 'Perianth bristles 6 or 7, ca. 2 × as long as nutlet']



#-------------------------------------------
# using date & pandas
import re
import numpy as np
import pandas as pd

def function(x):
    # 04/20/2009; 04/20/09; 4/20/09; 4/3/09; 4-13-82
    if re.search(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', x) is not None:
        return re.search(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', x).group()
    # Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    elif re.search(r'\d{,2}/\d{4}', x) is not None:
        return re.search(r'\d{,2}/\d{4}', x).group()
    # Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
    elif re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z-.\s]*\d{,2}[-,\s]*\d{4}', x) is not None:
        return re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z-.\s]*\d{,2}[-,\s]*\d{4}', x).group().strip()
    # 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    elif re.search(r'\d+\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.]*\s\d{4}', x) is not None:
        return re.search(r'\d+\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.]*\s\d{4}', x).group()
    # Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    elif re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}\w{2},\s\d{4}', x) is not None:
        return re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}\w{2},\s\d{4}', x).group()
    # Feb 2009; Sep 2009; Oct 2010    
    elif re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', x) is not None:
        return re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', x).group()
    # 2009; 2010
    elif re.search(r'\d{4}', x) is not None:
        return re.search(r'\d{4}', x).group()
    else:
        return np.nan

df2['new'] = df2['original'].apply(function)
