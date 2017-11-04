import os
import sys
import gensim
from gensim.models import Word2Vec

def tokenize_data():
	file_names = os.listdir("/home/yatharth/ASU/sml/project/100_Author/")
	tokens = []
	for file_name in file_names:
		word_list = []

		os.system("java -cp ../POS/stanford-postagger-full-2015-04-20/stanford-postagger.jar edu.stanford.nlp.process.PTBTokenizer " + "/home/yatharth/ASU/sml/project/100_Author/"+ file_name + ">" + "/home/yatharth/ASU/sml/project/100_Author_Token/" +file_name +"_token.txt" )
		
		# break
	print tokens

# tokenize_data()
def learnW2V():

	file_names = os.listdir("/home/yatharth/ASU/sml/project/100_Author_Token/")
	tokens = []
	for file_name in file_names:
		word_list = []
		
		with open("/home/yatharth/ASU/sml/project/100_Author_Token/"+file_name) as fp:
			for line in fp.readlines():
				word_list.append(line.strip('\n'))
		tokens.append(word_list)	
	print tokens

	model = gensim.models.Word2Vec(tokens, min_count=3,size=300,workers=4)
	# print len(tokens)


	print(model.similarity('languages', 'Thesis'))

learnW2V()