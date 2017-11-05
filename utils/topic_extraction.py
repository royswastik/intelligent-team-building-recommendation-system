__author__ = 'Swastik'
from gensim import corpora, models

def generate_document_term_matrix(texts):
    """texts is a list of documents, where each document corresponds to text in that document"""
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
    # print(ldamodel.print_topics(num_topics=3, num_words=3))
    return ldamodel