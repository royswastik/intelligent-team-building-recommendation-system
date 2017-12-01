__author__ = 'Yatharth'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import operator
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
import itertools
from author_collab import *
# nodes = hash_obj.keys()
nodes = []
def create_node():
	path = "../data/author/filtered_text_token/"
	file_names = os.listdir(path)
	for file_name in file_names:
		nodes.append(file_name.split(".")[0])

	G.add_nodes_from(nodes)

edgeList = []
sorted(nodes)
def add_edges():
	for node in nodes:

		if int(node) in  hash_obj.keys():
		
			for key, val in hash_obj[int(node)].iteritems():
				edgeList.append((int(node),key,1/float(val)))
		else:
			print "not found-->", node
	G.add_weighted_edges_from(edgeList)


# def findMinSum(adjMat,sub_graphs):
# 	print adjMat




create_node()
add_edges()
adjMat = dict(nx.all_pairs_dijkstra_path_length(G))

teamSize = 4
leastSumDistance = float("inf")
bestTeam = []
allBestTeam = []

for node in nodes:

	perNodeBestTeamSum = 0
	perNodeBestTeam = [int(node)]

	perDictSum = 0
	minDictSum = 1000000

	curLen = len(perNodeBestTeam)
	teamMem = -10
	noCandidates = 0
	while len(perNodeBestTeam) < teamSize and not noCandidates:
		candidates = []
		for i in xrange(len(perNodeBestTeam)):
			sorted_node = sorted(adjMat[int(perNodeBestTeam[i])].items(), key=operator.itemgetter(1))
			for subNode in sorted_node:

				if int(subNode[0]) not in perNodeBestTeam:
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

print allBestTeam
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
