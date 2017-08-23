import nltk

# BASICS
#---------------------------------------
# types of features in text classification
# 1) Words 
    # stopwords
    # normalisation (lowercase or not)
    # stemming/lemmatising or not
    # Caps or not
    # POS in a sentence
    # Grammatical structure
    # Grouping of words of same meaning (semantics), other e.g., dates


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


# Jaccard Distance, more: https://engineerbyday.wordpress.com/2012/01/30/how-spell-checkers-work-part-1/#Jaccard
nltk.jaccard_distance(set(nltk.ngrams(word1, n=4)),
                      set(nltk.ngrams(word2, n=4))) #shorter the distance, closer the match (0 to 1)
                      
                      
# Edit Distance
nltk.edit_distance(entries[0], a) #shorter distance, closer the match (0 to len(word))


# CLASSIFICATION
#---------------------------------------
from nltk.classify import NaiveBayesClassifier
# nltk naive bayes have a useful function to show most informative features
classifier.show_most_informative_features()



# Using Count Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Fitting the CountVectorizer tokenizes each document by finding all sequences of characters 
# of at least two letters or numbers separated by word boundaries. 
# Converts everything to lowercase and builds a vocabulary using these tokens. 
vect = CountVectorizer().fit(X_train)
print vect.get_feature_names() # give a list of feature names

X_train_vectorized = vect.transform(X_train)
print vect.vocabulary_ # gives a dict of feature names with frequency
print vect.vocabulary_.items() # gives pairs of key values in tuples instead, within a list

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)
predictions = model.predict(vect.transform(X_test))
print('AUC: ', roc_auc_score(y_test, predictions))


# TF-IDF (Term frequency-inverse document frequency)
    # High weight is given to terms that appear often in a particular document, 
        # but don't appear often in the corpus (all documents). 
    # Features with low tf–idf are either commonly used across all documents 
        # or rarely used and only occur in long documents.
# TF-IDF can reduce the number of features required to train a model
from sklearn.feature_extraction.text import TfidfVectorizer
# min_df, a minimum document frequency of < 5
# extracting 1-grams and 2-grams
vect = TfidfVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)

# Use CountVectorizor to find three letter tokens, remove stop_words, 
# remove tokens that don't appear in at least 20 documents,
# remove tokens that appear in more than 20% of the documents
vect = CountVectorizer(min_df=20, max_df=0.2, stop_words='english', 
                       token_pattern='(?u)\\b\\w\\w\\w+\\b') # (?u) refers to unicode
                       
                       
                       
                       

# SEMANTICS
#---------------------------------------
# semantic text similarity using WordNet
# http://www.nltk.org/howto/wordnet.html

# Path Similarity (highest 0.5, lowest near but not 0)
import nltk
from nltk.corpus import wordnet as wn

deer = wn.synset('deer.n.01')
elk = wn.synset('elk.n.01')
horse = wn.synset('horse.n.01')

deer.path_similarity(elk)   # 0.5
deer.path_similarity(horse) # 0.14

# Lin Similarity
# Lowest Common Subsumer (find closest ancestor)


# Collocations & Distributions Similarity
    # two words that occur frequently in similar context are more likely to be semantically related
    
    
# TOPIC MODELING
#---------------------------------------
# Coarse level analysis of what's in a text collection
# A document is a mixture of topics
# A text clustering problem
# Different models available
# Topic output are just word distributions: interpretation is subjective

# Given: Corpus, Number of Topics
# Not Given: Topic Names, Topic Distribution for each document

# Preprocessing
    # Tokenize, normalize
    # Stop words removal (common works in a domain)
    # Stemming
# Build Document Term Matrix
    # Convert document has what words > what words in each document
# Build LDA Model

# Latent Dirichlet Allocation
    # A type of generative model
    # Choose length of document 
    # Choose mixture of topic for document
    # Use topic's multinomial distribution to output words to fill topics's quota
        # for a particular document, 40% of the words come from topic A, then you use that topic A's multinomial distribution to output the 40% of the words. 
    # LDA is a very powerful tool and a text clustering tool that is fairly commonly used as the first step to understand what a corpus is about. 
    # LDA can also be used as a feature selection technique for text classification and other tasks
        
# So once you have built the mapping between the terms and documents, then suppose you have a set of pre-processed text documents in this variable doc_set. 
# Then you could use gensim to learn LDA this way. You could import gensim and specifically you import the corpora and the models. 
# First you create a dictionary, dictionary is mapping between IDs and words. 
# 
# Then you create corpus, and corpus you create going through this, all the documents in the doc_set, 
# and creating a document to bag of words model. 
# This is the step that creates the document term matrix.
#  Once you have that, then you input that in the LdaModel call, so that you use a gensim.models LdaModel, 
#  where you also specify the number of topics you want to learn. So in this case, we said number of topics is going to be four, 
#  and you also specify this mapping, the id2word mapping. That's a dictionary that is learned two steps ahead. 
# 
# Once you have learned that, then that's it, and you can say how many passes it should go through. 
# And there are other parameters that I would encourage you to read upon. But once you have defined this ldamodel,
#  you can then use the ldamodel to print the topics. So, in this particular case, we learnt four topics. 
#  And you can say, give me the top five words of these four topics and then it will bring that one out for you. 
# 
# ldamodel model can also be used to find topic distributions of documents. 
# So when you have a new document and you apply the ldamodel on it, so you infer it. 
# You can say, what was the topic distribution, across these four topics, for that new document. 

