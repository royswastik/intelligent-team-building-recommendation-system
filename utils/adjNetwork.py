__author__ = 'Yatharth'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import operator
import networkx as nx

# G = nx.Graph()
import matplotlib.pyplot as plt
import itertools
# from author_collab import *
from hindex import *

# from author_cite_map import *
from author_collaboration_cite_map import *
# from paper_cite_map import *

# nodes = hash_obj.keys()
def create_node(G):
	nodes = []
	# path = "data/author/filtered_text_token/"
	path=  os.path.join(os.path.dirname(__file__), '../data/author/author_text_full_token/')

	# path = "../data/author/author_text_full_token/"

	file_names = os.listdir(path)
	for file_name in file_names:

		if int(file_name.split(".")[0]) in hash_obj.keys():
			nodes.append(int(file_name.split(".")[0]))
		# else:
		# 	print file_name
	G.add_nodes_from(nodes)
	return nodes
edgeList = []
notEdgeList=[]

def create_node_with_array(G,arrayNode):

	G.add_nodes_from(arrayNode)
	# print len(arrayNode)

def add_edges(G):
	for node in nodes:

		if int(node) in  hash_obj.keys():
		
			for key, val in hash_obj[int(node)].iteritems():
				if int(key) in nodes:
					edgeList.append((int(node),key,float(1/float(val))))
				else:
					notEdgeList.append(int(key))
		else:
			print "not found-->", node
	G.add_weighted_edges_from(edgeList)


def add_edges_with_array(G,arrayNode):
	edgeList =[]
	for node in arrayNode:

		if int(node) in  hash_obj.keys():
		
			for key, val in hash_obj[int(node)].iteritems():
				if int(key) in arrayNode:
					edgeList.append((int(node),key,float(1/float(val))))
				else:
					notEdgeList.append(int(key))

		else:
			print "not found-->", node
	# print len(edgeList)
	# print len(notEdgeList)
	G.add_weighted_edges_from(edgeList)

def graph_clus(G,arrayNode,teamSize=2):
	adjMat = dict(nx.all_pairs_dijkstra_path_length(G))
	
	leastSumDistance = float("inf")
	bestTeam = []
	allBestTeam = []

	for node in arrayNode:

		# print "node -->", node
		perNodeBestTeamSum = 0
		perNodeBestTeam = [int(node)]

		perDictSum = 0
		minDictSum = 1000000

		curLen = len(perNodeBestTeam)
		teamMem = -10
		# print "node best", perNodeBestTeam
		# print "---",adjMat[int(perNodeBestTeam[0])]
		noCandidates = 0
		while len(perNodeBestTeam) < teamSize and not noCandidates:
			candidates = []
			for i in xrange(len(perNodeBestTeam)):
				sorted_node = sorted(adjMat[int(perNodeBestTeam[i])].items(), key=operator.itemgetter(1))
				for subNode in sorted_node:
					if int(subNode[0]) in arrayNode and int(subNode[0]) not in perNodeBestTeam:
						# if int(subNode[0]) ==5561:
						# 	print 'found'

						candidates.append(subNode)
						break

			bestCandidates = []
			sumPairs = 0
			if candidates!=[]:
				for data1 in candidates:
					for data2 in perNodeBestTeam:
						if int(data1[0]) in adjMat and int(data2) in adjMat[int(data1[0])]:
							sumPairs+= adjMat[int(data1[0])][int(data2)]

						elif int(data2) in adjMat and int(data1[0]) in adjMat[int(data2)]:
							sumPairs+= adjMat[int(data2)][int(data1[0])]
						else:
							sumPairs+=10000


					bestCandidates.append((data1[0],sumPairs+perNodeBestTeamSum))
				# print bestCandidates,"<-- bestCandidates"
				bestCandidates.sort(key=lambda x: x[1])
				perNodeBestTeamSum += bestCandidates[0][1]
				perNodeBestTeam.append(bestCandidates[0][0])
			else:
				noCandidates = 1
				break

		if noCandidates == 0 and perNodeBestTeamSum <=leastSumDistance:
			leastSumDistance =perNodeBestTeamSum
			allBestTeam.append({'team':perNodeBestTeam,'distance':perNodeBestTeamSum})

	# print allBestTeam[-1]
	# sumBest = 0
	# print "\n\n"
	# print "----------------"
	# for teams in allBestTeam:
	# 	sumteam = 0
	# 	H = G.subgraph(teams['team'])
	# 	print "closeness cent",nx.closeness_centrality(H)
	# 	for (u, v, wt) in H.edges.data('weight'):
	# 		print u,"-->",v,"-->",wt

	# 	for bestMem in teams['team']:
	# 		sumteam+= hindex[bestMem]
	# 	print "hindex",sumteam
	# 	print "dis",teams['distance']


	# print allBestTeam[len(allBestTeam)-2]['team']
	# H = G.subgraph(allBestTeam[len(allBestTeam)-2]['team'])
	# print H.edges()
	# nx. nx.draw_networkx_edges(H, pos=nx.spring_layout(G))
	# plt.show()
	return allBestTeam[-1]['team']

# graph_clus()











				# candidates.append()
	# 		if sorted_node!=[]:
	# 			if perDictSum + sorted_node[0][1]  < minCurTeamSum:
				
	# 				minCurTeamSum = perDictSum + sorted_node[0][1]
	# 				teamMem = sorted_node[0][0]
					
	# 		else:
	# 			teamMem = -10
	# 	if teamMem !=-10:
	# 		perDictSum +=minCurTeamSum	
	# 		perNodeBestTeam.append(teamMem)
	# 	curLen=len(perNodeBestTeam)


	
	# if perDictSum<=leastSumDistance:
	# 	# print "forrr->>", node,"\n"
	# 	# print perDictSum
	# 	# print bestTeam
	# 	bestTeam = perNodeBestTeam
	# 	allBestTeam.append({'team':bestTeam,'distance':perDictSum})
# print bestTeam
# print leastSumDistance
# print len(allBestTeam)
# print allBestTeam







# for sub_nodes in itertools.combinations(G.nodes(),teamSize):
# 	# print int(sub_nodes[1])
# 	# print adjMat[int(sub_nodes[0])]
# 	isConnected = iset(sub_nodes) <= int(adjMat[sub_nodes[0]].keys())
# 	print isConnected
# 	print '----------'
# 	# if isConnected:

# findMinSum(adjMat,sub_graphs)
# findMinMST(adjMat,sub_graphs)
