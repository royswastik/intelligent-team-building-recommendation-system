__author__ ='Yatharth'

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from utils.adjNetwork import *
from utils.HAC import *
from utils.SpectralClustering import *

from train.doc2vec import fit_doc2vec
import networkx as nx
from utils.hindex import *
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from train.doc2vec import get_cosine_similarity

from train.doc2vec import get_similarity_with_team

def runFinal(thres=0,inputSize=4):
	G = nx.Graph()
	probSt = "Need engineers to work on Question Answering System Job responsibilities involve Information Retrieval create dialog systems, machine translation techniques"
	authors = fit_doc2vec(probSt)
	# print authors
	authorWithSim = []

	resultH = []
	resultS = []
	resultVal = []
	# for tSize in range(100,1300,100):

	for author in authors[1:500]:
		# if author[1]>=thres:
		authorWithSim.append(int(author[0]))
	print authorWithSim
	create_node_with_array(G,authorWithSim)
	add_edges_with_array(G,authorWithSim)
	authorDict =  dict(authors)

	resultLabel = ['Heirarchical','Spectral','Graph MinSum']

# 		# print authorWithSim
# 	################################################################################
# 		##calling code for Heirarchical##
# 	###############################################################################
	# adjList = data_mat_HAL(G,authorWithSim)
	# teamHClus =  hal_clustering(adjList,4,authorWithSim)
	# sumTeam = 0
	# sumSim = 0
	# print teamHClus
	# for team in teamHClus:
	# 	# print authorDict[str(team)]
	# 	sumSim+= authorDict[str(team)]
	# 	sumTeam+= hindex[team]
	# # resultVal.append(sumTeam)
	# print "team sim-->",sumSim
	# print "team H-index->",sumTeam

# ################################################################################
# 	## calling codde for graphG
# ################################################################################
# 	# print specclustering(authorWithSim)

	sumTeam = 0
	sumSim = 0
	teamSp = [5147, 5674, 2083, 2340] 
	print G.nodes()
	for data in teamSp:
		sumTeam+= hindex[data]
		sumSim+= authorDict[str(data)]
	print "team sim-->",sumSim
	print "team H-index->",sumTeam

# 	# resultVal.append(0)

# ################################################################################
# 	## calling codde for graphG
# ################################################################################
# 	print "------------------------------"
# 	teamGClus = graph_clus(G,authorWithSim,teamSize=4)
# # 	# print teamGClus
# 	sumTeam = 0
# 	sumSim = 0

# 	print teamGClus
# 	for team in teamGClus:
# 		sumSim+= authorDict[str(team)]
# 		sumTeam+= hindex[team]

# 		resultH.append(sumTeam)
# 		resultS.append(sumSim)
# 	print "team sim-->",sumSim
# 	print "team H-index->",sumTeam

# 	print sumTeam
##### Plot data ####
	# plt.ylabel('H-Index')
	# plt.bar(resultLabel,resultVal)
	# plt.show()
	# print resultH
	# print resultS
	# teamRes=authorWithSim[:4]
	# sumTeam = 0
	# sumSim = 0
	# for team in teamRes:
	# 	sumSim+= authorDict[str(team)]		
	# 	sumTeam+= hindex[int(team)]
	# print "sim-->",sumSim
	# print "h index -- >",sumTeam

	# print teamSp
	H = G.subgraph(teamSp)
	nx. nx.draw(H,  pos = nx.random_layout(G))
	plt.show()
	# print H.nodes()
	print "closeness cent",nx.closeness_centrality(H)
runFinal(0,4)
	

# creating graph using adjNetwork
# create_node() 
# add_edges()


