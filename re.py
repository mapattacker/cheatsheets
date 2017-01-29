import re

# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.youtube.com/watch?v=kWyoYtvJpe4

  # .     (dot) matches any character.
  # +     Matches 1 or more occurrence of preceding expression.
  # a|b	  Matches either a or b.
  # \w	  Matches word characters (numbers & alphabets).
  # \W	  Matches nonword characters.
  # \d	  Matches digits. Equivalent to [0-9].
  # \D	  Matches nondigits.
  # \s    Matches whitespace
  # \S    Matches non-whitespace
  
phone = "2004-959-559 # This is Phone Number"


# match; output if result at start of string
num = re.match(r'\w\w\w', phone)
print num.group() #output '200'

# search; output first result in string
num = re.search(r'...4', phone)
print num.group() #output '2004'

num = re.search(r'\sThis', phone)
print num.group() #output ' This'

num = re.search(r'.+559', phone)
print num.group() #output '2004-959-559'

# findall; output all results in a list
num = re.findall(r'2004|Phone', phone)
print num #output ['2004', 'Phone']

# replace
num = re.sub(r'\W', '', phone)  #3 arguments
print num
