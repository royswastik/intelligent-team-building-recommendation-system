__author__ = 'Swastik'
from gensim import corpora, models
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import utils.text_extractor as TextExtractor
import constants
import os
from utils import tokenizer as Tokenizer
from utils import tokenFixer as TokenFixer
from utils import nlp_parser as NLPParser

def train_tf_idf(docs):
    dictionary = corpora.Dictionary(docs)
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    # Run tf-idf
    tfidf = models.TfidfModel(corpus)
    return tfidf, corpus, dictionary

def plot_word_cloud(tf_idf_model, corpus, dictionary, filename="words_filtered"):
    predict = [item for sublist in corpus for item in sublist]
    # top_words = np.sort(np.array(tf_idf_model[corpus[len(corpus)-1]],dtype = [('word',int), ('score',float)]),order='score')[::-1]
    top_words = np.sort(np.array(tf_idf_model[predict],dtype = [('word',int), ('score',float)]),order='score')[::-1]
    word_dict = {}

    for word,score in top_words:
        word_dict[dictionary[word]] = score
    wc = WordCloud(background_color="white",random_state=5,max_words=5000).fit_words(word_dict)
    # wc = WordCloud(background_color="white",random_state=5,max_words=2000).fit_words([(dictionary[word],score)
    #     for word,score in top_words])

    plt.imshow(wc.recolor(random_state=5))
    plt.axis("off")
    wc.to_file(filename+".png")

def create_word_cloud_from_words(word_list, title="Extracted Words"):
    word_dict = create_word_freq_dict(word_list)
    wc = WordCloud(background_color="white",random_state=5,max_words=5000).fit_words(word_dict)
    plt.title(title)
    plt.imshow(wc.recolor(random_state=5))
    plt.axis("off")
    plt.show()

def create_word_freq_dict(word_list):
    word_dict = {}
    for word in word_list:
        if word in {'proceeding', "method","result", "algorithm", "figure", "association", "problem", "weight", "function", "target", "domain", "translation", "grammar"}:
            continue
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

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

def test2():
    docs =  []
    count = 0
    for fileName in os.listdir(os.path.join(constants.DATA_PATH,'author_topic_filtered')):
        if count >= 0:
            doc =  TextExtractor.read_all_text(os.path.join(constants.DATA_PATH,'author_topic_filtered', fileName)).split(",")
            docs.append(doc)
        if count >= 600:break
        print count
        count += 1
    tf_idf, corpus, dictionary = train_tf_idf(docs)
    plot_word_cloud(tf_idf, corpus, dictionary, 'filtered_wordcloud')

#Run TF IDF on paper titles
def test3():
    docs =  []
    count = 0

    with open(os.path.join(constants.DATA_PATH,'paper_ids.txt'), "r") as ins:
        for line in ins:
            line = line[9:-5]
            print(line)
            # doc =  TextExtractor.read_all_text(os.path.join(constants.DATA_PATH,'author_topic_filtered', fileName)).split(",")
            docs.append(line.split(' '))
            # if count >= 600:break
            # print count
            count += 1
        line = []
    tf_idf, corpus, dictionary = train_tf_idf(docs)
    plot_word_cloud(tf_idf, corpus, dictionary, 'paper_title_wordcloud')

#Run Word2Vec on single document
def test4():
    text = TextExtractor.read_all_text(os.path.join(constants.DATA_PATH, 'author_topic_filtered', '1002.txt')).split(',')
    text2 = TextExtractor.read_all_text(os.path.join(constants.DATA_PATH, 'author_topic_filtered', '1004.txt')).split(',')
    docs = []
    docs.append(text)
    docs.append(text2)
    tf_idf, corpus, dictionary = train_tf_idf(docs)
    plot_word_cloud(tf_idf, corpus, dictionary, 'filtered_100_wordcloud')

def test5():
    # text1 = TextExtractor.read_all_text(os.path.join(constants.DATA_PATH, 'authors_topic', '1002.txt'))
    # tokens = Tokenizer.get_tokens(text1)
    # create_word_cloud_from_words(tokens, "Initial Tokens")
    #
    # tokens = Tokenizer.get_stopped_tokens(text1)
    # create_word_cloud_from_words(tokens, "Stop Words Removed")

    # tokens = Tokenizer.get_stemmed_tokens(text1)
    # create_word_cloud_from_words(tokens, "Stemmed Tokens")

    # tokens = TokenFixer.fix_broken_words(tokens)
    # nps = NLPParser.get_noun_phrases(text1)
    # create_word_cloud_from_words(nps, "Noun Phrases")

    tokens0 = TextExtractor.read_all_text(os.path.join(constants.DATA_PATH, 'author_topic_filtered', '1002.txt')).split(',')
    create_word_cloud_from_words(tokens0, "Topics")



if __name__ == '__main__':
    test5()