__author__ = 'Swastik'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from parser import publication_extractor as PubExtractor
from utils import topic_extraction as TopicExtractor


def test_topic_extraction():
    doc = PubExtractor.extract_publication("A00-1001")
    doc = [doc]
    topicModel = TopicExtractor.generate_document_term_matrix(doc)
    print(topicModel.print_topics(num_topics=3, num_words=3))


def __init__():
    test_topic_extraction()
