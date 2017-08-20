import nltk

# DEFAULT CORPUSES
#---------------------------------------
# Open window to select download of corpuses (colletion of writings) and packages in nltk
nltk.download()

from nltk.book import * # list books
text1 # list book
sent1 # list one sentence of text1

# all english words
from nltk.corpus import words
correct_spellings = words.words()


# FREQUENCY DISTRIBUTION
#---------------------------------------
freq = nltk.FreqDist(g)
print freq
# it gives a dictionary
FreqDist({u'endorsed': 2,
          u'Mortimer': 1,
          u'foul': 2,
          u'Heights': 5,
          u'four': 20,
          u'spiders': 1,
          u'railing': 3,})

# So it works like a dictionary
freq.keys() # get words without frequency
freq['endorsed'] # >>> 2
          
top10 = freq.most_common(300) # top n most common, arranged descending order



# STEMMING
#---------------------------------------
# stemming involved finding the root word
input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')

porter = nltk.PorterStemmer()
[porter.stem(t) for t in words1]
# ['list', 'list', 'list', 'list', 'list']



# LEMMATIZATION
#---------------------------------------
# lemmatising is a variant of stemming that makes all root words a word.
# stemming will sometimes make it not a word.

udhr = nltk.corpus.udhr.words('English-Latin1')

# Using Stemming
porter = nltk.PorterStemmer()
print [porter.stem(t) for t in udhr[:20]]
[u'univers',
 u'declar',
 u'of',
 u'human',
 u'right',
 u'preambl',
 u'wherea',
 u'recognit']

# Using Lemmatization
WNlemma = nltk.WordNetLemmatizer()
print [WNlemma.lemmatize(t) for t in udhr[:20]]
['Universal',
 'Declaration',
 'of',
 'Human',
 'Rights',
 'Preamble',
 'Whereas',
 'recognition']
 
# TOKENIZATION
#---------------------------------------
# splitting text into words or sentences

# Word Tokens
text11 = "Children shouldn't drink a sugary drink before bed."
print text11.split(' ')
['Children', "shouldn't", 'drink', 'a', 'sugary', 'drink', 'before', 'bed.']

print nltk.word_tokenize(text11)
['Children', 'should', "n't", 'drink', 'a', 'sugary', 'drink', 'before', 'bed', '.']

# Sentence Tokens
text12 = "This is the first sentence. A gallon of milk in the U.S. \
            costs $2.99. Is this the third sentence? Yes, it is!"
print nltk.sent_tokenize(text12)
['This is the first sentence.',
 'A gallon of milk in the U.S. costs $2.99.',
 'Is this the third sentence?',
 'Yes, it is!']
 
 
# PARTS OF SPEECH (POS)
#---------------------------------------
# grammer terms
# get definition and examples of terms
nltk.help.upenn_tagset('MD')

text11 = "Children shouldn't drink a sugary drink before bed."
text11 = nltk.word_tokenize(text11)
print nltk.pos_tag(text13)

[('Children', 'NNP'),
 ('should', 'MD'),
 ("n't", 'RB'),
 ('drink', 'VB'),
 ('a', 'DT'),
 ('sugary', 'JJ'),
 ('drink', 'NN'),
 ('before', 'IN'),
 ('bed', 'NN'),
 ('.', '.')]
 
 
# isalpha()
#---------------------------------------
# Gives boolean whether the string contains alpabets only
str = "this";  # No space & digit in this string
print str.isalpha() # True

str = "this is string example....wow!!!";
print str.isalpha() # False


# SPELL CHECKER ALGORITHMS
#---------------------------------------
# about ngrams
print set(nltk.ngrams('hello', n=3)) #trigram cos n=3
# set([('l', 'l', 'o'), ('e', 'l', 'l'), ('h', 'e', 'l')])


# Jaccard Distance
nltk.jaccard_distance(set(nltk.ngrams(word1, n=4)),
                      set(nltk.ngrams(word2, n=4))) #shorter the distance, closer the match (0 to 1)
                      
                      
# Edit Distance
nltk.edit_distance(entries[0], a) #shorter distance, closer the match (0 to len(word))