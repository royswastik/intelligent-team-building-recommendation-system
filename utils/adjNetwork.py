__author__ = 'Yatharth'
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import operator
import networkx as nx
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
				edgeList.append((int(node),key,{'weights':val}))
		else:
			print "not found-->", node
	G.add_edges_from(edgeList)


# def findMinSum(adjMat,sub_graphs):
# 	for subNodes in sub_graphs:





create_node()
add_edges()

adjMat = dict(nx.all_pairs_shortest_path(G))

teamSize = 5
leastSumDistance = float("-inf")
bestTeam = []
sub_graphs = [sub_nodes for sub_nodes in itertools.combinations(G.nodes(),teamSize)]
print sub_graphs

# findMinSum(adjMat,sub_graphs)
# findMinMST(adjMat,sub_graphs)
