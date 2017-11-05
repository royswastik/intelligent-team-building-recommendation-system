__author__ = 'Swastik'
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')

def get_tokens(document):
    raw = document.lower()
    tokens = tokenizer.tokenize(raw)
    return tokens

def get_stopped_tokens(document):
    tokens = get_tokens(document)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    return stopped_tokens


def get_stemmed_tokens(document):
    stopped_tokens = get_stopped_tokens(document)
    texts = [p_stemmer.stem(i) for i in stopped_tokens]
    return texts