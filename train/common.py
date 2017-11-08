__author__ = 'Swastik'
from gensim import corpora, models
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import utils.text_extractor as TextExtractor
import constants
import os

def train_tf_idf(docs):
    dictionary = corpora.Dictionary(docs)
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    # Run tf-idf
    tfidf = models.TfidfModel(corpus)
    return tfidf, corpus, dictionary

def plot_word_cloud(tf_idf_model, corpus, dictionary):
    top_words = np.sort(np.array(tf_idf_model[corpus[len(corpus)-1]],dtype = [('word',int), ('score',float)]),order='score')[::-1]
    word_dict = {}

    for word,score in top_words:
        word_dict[dictionary[word]] = score
    wc = WordCloud(background_color="white",random_state=5,max_words=2000).fit_words(word_dict)
    # wc = WordCloud(background_color="white",random_state=5,max_words=2000).fit_words([(dictionary[word],score)
    #     for word,score in top_words])

    plt.imshow(wc.recolor(random_state=5))
    plt.axis("off")
    wc.to_file("words.png")

def test():
    docs = []
    doc1 =  TextExtractor.read_all_text(os.path.join(constants.TEST_OUTPUT, "10.txt")).split(",")
    doc2 =  TextExtractor.read_all_text(os.path.join(constants.TEST_OUTPUT, "100.txt")).split(",")
    doc3 =  TextExtractor.read_all_text(os.path.join(constants.TEST_OUTPUT, "101.txt")).split(",")
    docs.append(doc1)
    docs.append(doc2)
    docs.append(doc3)
    tf_idf, corpus, dictionary = train_tf_idf(docs)
    plot_word_cloud(tf_idf, corpus, dictionary)

if __name__ == '__main__':
    test()