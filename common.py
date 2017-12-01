__author__ = 'Swastik'

import nltk

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
lemmatizer = nltk.WordNetLemmatizer()
from utils import text_extractor as TextExtractor
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')
