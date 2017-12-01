import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import os
import re
import nltk
from common import *
import publication_extractor
from textblob import TextBlob
import constants

# from nltk.tag.stanford import NERTagger
# st = NERTagger('ner/all.3class.distsim.crf.ser.gz', 'ner/stanford-ner.jar')
__author__ = 'Swastik'
# from nltk.tag import StanfordNERTagger
# st = StanfordNERTagger('sner/english.all.3class.distsim.crf.ser.gz', 'sner/stanford-ner.jar',
# 					   encoding='utf-8')

# tagger = ner.HttpNER(host='localhost', port=8080)
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
        if len(np) > 5 and  re.match('^[a-z\d\-_\s]+$', np) is not None:
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
    return nltk.ne_chunk(text)
    # for sent in nltk.sent_tokenize(text):
    #     tokens = nltk.tokenize.word_tokenize(sent)
    #     tags = st.tag(tokens)
    #     # for tag in tags:
    #     #     if tag[1]=='PERSON': print tag
    #     #     if tag[1]=='LOCATION': print tag

def write_author_noun_phrases():
    readDir = os.path.join(constants.DATA_PATH, "authors_text")
    outDir = os.path.join(constants.DATA_PATH, "authors_topic")
    if not os.path.exists(readDir):
        print("authors_text folder not found. Use parser/AuthorPaperText to generate authors_text.")
    if not os.path.exists(outDir):
        print("Generating Output Directory")
        os.makedirs(outDir)

    # count = 0
    for filename in os.listdir(readDir):
        # if count > 3: break
        if filename[0]>=2:
            authorContentPath = os.path.join(readDir, filename)
            text = TextExtractor.extract_corrected_text(authorContentPath)
            nounPhrases = get_noun_phrases(text)
            content = ",".join(nounPhrases)
            outPath = os.path.join(constants.DATA_PATH, "authors_topic", filename)
            TextExtractor.write_to_file(content, outPath)
            # print filename
            # count += 1

if __name__ == "__main__":
    write_author_noun_phrases()
    # text = publication_extractor.extract_corrected_text("A00-1001")
    # nounPhrases = get_noun_phrases(text)
    # filtered = [elem for elem in nounPhrases if len(elem) > 5 and  re.match('^[a-z\d\-_\s]+$', elem) is not None]
    # for np in filtered:
    #     print(np)
