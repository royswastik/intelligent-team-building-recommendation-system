__author__ = 'Swastik'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# from parser import publication_extractor as PubExtractor
# from utils import topic_extraction as TopicExtractor
from common import *


def test_topic_extraction(pub_id):
    text = PublicationExtractor.extract_publication(pub_id)
    stemmedTokens = Tokenizer.get_stemmed_tokens(text)
    doc = stemmedTokens
    doc = [doc]
    topicModel = TopicExtractor.generate_document_term_matrix(doc)
    print(topicModel.print_topics(num_topics=10, num_words=3))
    print(len(topicModel.print_topics(num_topics=10, num_words=3)))

def __init__():
    test_topic_extraction("A00-1001")

if __name__ == "__main__":
    test_topic_extraction("A00-1001")
    test_topic_extraction("A00-1016")