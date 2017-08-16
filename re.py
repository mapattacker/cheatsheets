import re

# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.youtube.com/watch?v=kWyoYtvJpe4

  # .     (dot) matches any character.
  # *     Matches 0 or more occurrence of preceding expression.
  # +     Matches 1 or more occurrence of preceding expression.
  # ?     Matches 0 or 1 occurences of preceding expression.
  # {n}   Matches exactly n reptitions
  # {n,}  At least n times
  # {,n}  At most n times
  # {m,n} At least m and at most n repetitions (e.g., \d{1,2} means get 1 or 2 digits only)
  # ^     Match first character in line
  # $     Match last character of string
  # []    Matches any charcters in the square brackets
  # ()    Groups regular expressions and remembers matched text / output & find only characters in brackets.
  # (?:)  Outputs not just within brackets, but the entire string
  # a|b	  Matches either a or b.
  
  # \     backslash changes search code into real symbol (eg., \$)
  
  # [^A-Z] does not match alphabets A to Z (^ means does not)
  
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


#-------------------------------------------
phone = "2004-959-559 # This is Phone Number"
email = 'this is an bah bah email nick19a@gmail.com the end foo@gmail.com.'


#-------------------------------------------
# match; output if result at start of string
num = re.match(r'\w\w\w', phone)
print num.group() #output '200'


#-------------------------------------------
# search; output first result in string
# can use s.split(' ') to split the text into individuals words first
num = re.search(r'...4', phone)
print num.group() #output '2004'

num = re.search(r'\sThis', phone)
print num.group() #output ' This'

num = re.search(r'.+559', phone)
print num.group() #output '2004-959-559'

result = re.search(r'\w+@[\w.]+', email)  #find all word characters and dot after @
print result.group()  #output 'nick19a@gmail.com'

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
