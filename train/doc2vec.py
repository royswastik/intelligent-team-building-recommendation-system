__author__ = 'Yatharth'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from gensim.models import Doc2Vec
import gensim.models.doc2vec
# from collections import OrderedDic
from gensim.models.doc2vec import LabeledSentence
import multiprocessing

def getDocuments():
	path = "../data/"
	file_names = os.listdir(path)
	documents = []
	for file_name in file_names:
		word_list = []
		
		with open(path+file_name) as fp:
			for line in fp.readlines():
				word_list.append(line.strip('\n'))
			documents.append( LabeledSentence(words=word_list, tags=[file_name.split(".")[0]]) )

	return documents

def train_word2Vec():
	"""Trains Doc2Vec Model for all documents"""

	documents = getDocuments()
	model = Doc2Vec(size=300, window=10, min_count=1, workers=4)
	model.build_vocab(documents)
	for epoch in range(20):
		model.train(documents,total_examples=model.corpus_count,epochs=epoch)
	# pass
	vecTest= model.infer_vector(["natural","disasters","deaths","bombings","elections","financial","fluctuations"])
	print vecTest
	sims = model.docvecs.most_similar([vecTest],topn = 100)
	print sims

train_word2Vec()