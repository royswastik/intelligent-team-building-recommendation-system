__author__ = 'Swastik'
import utils.nlp_parser as NLPParser

def parse_query_text(query_string):
    noun_phrases = NLPParser.get_noun_phrases(query_string)
    named_entities = NLPParser.get_named_entities(query_string)
    pass