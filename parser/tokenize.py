__author__ = 'Yatharth'
# import os,sys,inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir)
import os
import sys
# import gensim
# from gensim.models import Word2Vec

def tokenize_data():
	path = "../data/author/authors_topic/"
	file_names = os.listdir(path)
	tokens = []
	for file_name in file_names:
		word_list = []

		os.system("java -cp /home/yatharth/ASU/sml/project/2014/POS/stanford-postagger-full-2015-04-20/stanford-postagger.jar edu.stanford.nlp.process.PTBTokenizer " + path+"/"+ file_name + ">" + "../data/author/author_topic_token/" +file_name +"_token.txt" )
		
		# break
	print tokens

# tokenize_data()
def learnW2V():

	file_names = os.listdir("../data/author/author_topic_token/")
	tokens = []
	for file_name in file_names:
		word_list = []
		
		with open("../data/author/author_topic_token/"+file_name) as fp:
			for line in fp.readlines():
				word_list.append(line.strip('\n'))
		tokens.append(word_list)	
	print tokens

	model = gensim.models.Word2Vec(tokens, min_count=3,size=300,workers=4)
	# print len(tokens)


	print(model.similarity('languages', 'Thesis'))

# learnW2V()