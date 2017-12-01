__author__ = 'Yatharth'
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from utils import nlp_parser as NLPParser, tokenFixer as TokenFixer

from sklearn.metrics.pairwise import cosine_similarity

import itertools
from gensim.models import Doc2Vec
import gensim.models.doc2vec
from gensim import corpora
from gensim.models.doc2vec import LabeledSentence
import multiprocessing


def getDocuments():
    path = "../data/author/filtered_text_token/"
    file_names = os.listdir(path)
    documents = []
    for file_name in file_names:
        word_list = []

        with open(path + file_name) as fp:
            for line in fp.readlines():
                word = line.strip(',').strip('\n')
                if word != '':
                    word_list.append(word)
            if word_list != []:
                documents.append(LabeledSentence(words=word_list, tags=[file_name.split(".")[0]]))

    return documents


def train_word2Vec():
    """Trains Doc2Vec Model for all documents"""
    documents = getDocuments()
    # print documents
    print len(documents)
    model = Doc2Vec(size=300, window=10, min_count=1, workers=4)
    model.build_vocab(documents)
    for epoch in range(30):
        model.train(documents, total_examples=model.corpus_count, epochs=epoch)
    # pass
    model.save('Authors.doc2vec')
    vecTest = model.infer_vector(
        ["birthday", "answer", "useful  url information", "answer", "answer", "variety", "birthday", "question",
         "example", "conventional  cqa policy", "answer", "purpose", "answer", "alternative", "answer",
         "in-depth analysis"])
    print vecTest
    sims = model.docvecs.most_similar([vecTest], topn=100)
    print sims


# train_word2Vec()

def testModel():
    path = "../data/author/filtered_text_token/"
    word_list = []
    with open(path + "10.txt_token.txt") as fp:
        for line in fp.readlines():
            word = line.strip(',').strip('\n')
            if word != '':
                word_list.append(word)

    # word_list =["attitude","label","table","summarization","algorithm","sent","ment-opinion","segment","answer","sentence","cluster","sentence","similar","process"]
    # print word_list
    model = Doc2Vec.load('Authors.doc2vec')
    vecTest = model.infer_vector(word_list)
    # print vecTest
    sims = model.docvecs.most_similar([vecTest], topn=976)
    print sims


# testModel()

# TODO - check how similar two documents are
def get_similarity_score(doc1, doc2):
    model = Doc2Vec.load('Authors.doc2vec')
    tokens1 = doc1.split[" "]
    tokens2 = doc2.split[" "]
    s1 = model.infer_vector(tokens1, alpha=0.025, min_alpha=0.025, steps=20)
    s2 = model.infer_vector(tokens2, alpha=0.025, min_alpha=0.025, steps=20)
    print(cosine_similarity(s1, s2))


def lda():
    documents = getDocuments()
    docFlat = list(itertools.chain(*documents))
    dictionary = corpora.Dictionary(docFlat)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in docFlat]
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=20, id2word=dictionary, passes=10)
    ldamodel.save('lda.model')
    ldamodel.print_topics(num_topics=20, num_words=10)


# lda()

def get_cosine_similarity(input1, docs):
    # path_doc2vec=  os.path.join(os.path.dirname(_file_), 'Authors_final.doc2vec')
    # model = Doc2Vec.load('Authors.doc2vec')
    inputTokens = get_tokens_from_docs([input1])
    docTokens = get_tokens_from_docs(docs)
    # vec1 = model.infer_vector(inputTokens)

    # vec2 = model.infer_vector(docTokens)
    return 0
    # return cosine_similarity(vec1, vec2)


def get_tokens_from_docs(docs):
    result = []
    for doc in docs:
        corrected_nps = TokenFixer.fix_broken_words(NLPParser.get_noun_phrases(doc))[0]
        for np in corrected_nps:
            result.extend(np.split(" "))
    return result


if __name__ == '__main__':
    score = get_cosine_similarity("I am a man who loves machine learning", ["I am an author", "I need natural language processing engineers"])
    print(score)
