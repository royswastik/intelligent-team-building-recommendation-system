__author__ = 'Swastik'
import nltk
import utils.publication_extractor as PublicationExtractor
import utils.text_extractor as TextExtractor
import utils.topic_extraction as TopicExtractor
import utils.tokenizer as Tokenizer
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
lemmatizer = nltk.WordNetLemmatizer()
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')
