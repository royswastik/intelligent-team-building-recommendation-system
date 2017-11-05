import re
import nltk
from common import *
import publication_extractor
from textblob import TextBlob
import ner
# from nltk.tag.stanford import NERTagger
# st = NERTagger('ner/all.3class.distsim.crf.ser.gz', 'ner/stanford-ner.jar')
__author__ = 'Swastik'
# from nltk.tag import StanfordNERTagger
# st = StanfordNERTagger('sner/english.all.3class.distsim.crf.ser.gz', 'sner/stanford-ner.jar',
# 					   encoding='utf-8')

tagger = ner.HttpNER(host='localhost', port=8080)
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)
sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'


def get_noun_phrases(text):
    toks = nltk.regexp_tokenize(text, sentence_re)
    postoks = pos_tag(toks)
    # print postoks
    tree = chunker.parse(postoks)
    terms = get_terms(tree)
    noun_phrases = []
    for term in terms:
        np =  " ".join(term)
        noun_phrases.append(np)
    return noun_phrases

def get_corrected_noun_phrases(noun_phrases):
    pass

def pos_tag(tokens):
    return nltk.tag.pos_tag(tokens)

def get_parse_tree(postoks):
    return chunker.parse(postoks)

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    # word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in en_stop)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

def get_named_entities(text):
    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': print tag
            if tag[1]=='LOCATION': print tag

if __name__ == "__main__":
    text = publication_extractor.extract_corrected_text("A00-1001")
    nounPhrases = get_noun_phrases(text)
    filtered = [elem for elem in nounPhrases if len(elem) > 5 and  re.match('^[a-z\d\-_\s]+$', elem) is not None]
    for np in filtered:
        # b = TextBlob(np)
        print(np)
        # print(get_named_entities(np))
        # print("------")
    # print(nounPhrases)
    # get_noun_phrases("A quick brown fox jumps over the lazy dogs")
