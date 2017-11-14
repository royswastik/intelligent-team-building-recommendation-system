__author__ = 'Ishita'
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
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
print nodes



def add_edges():
    for node in nodes:

        if int(node) in hash_obj.keys():

            for key, val in hash_obj[int(node)].iteritems():
                edgeList.append((int(node), key, {'weights': val}))
        else:
            print "not found-->", node
    G.add_edges_from(edgeList)


# def findMinSum(adjMat,sub_graphs):
# 	for subNodes in sub_graphs:



def data_mat_HAL():

    adjList={}

    for node1 in nodes:
        for node2 in nodes:

            if int(node1) in hash_obj.keys() and int(node2) in hash_obj[int(node1)].keys():
                #adjList[int(node1)[int(node2)]] = adjMat[int(node1)][int(node2)]
                #print node1,"-------------", node2
                subdict= adjMat[int(node1)]

                if(subdict==null):
                    adjList[int(node1)]= subdict[int(node2)]

                else:
                    adjList[int(node1)].append({int(node2):subdict[int(node2)]})
                # print adjList[int(node1)]
                # print adjList
                # exit()
            elif int(node1) not in hash_obj.keys():
                adjList[int(node1)]=0


    print adjList
    # with open('adjList.csv', 'w') as a:
    #     a.write(str(adjList))


create_node()
add_edges()

adjMat = dict(nx.all_pairs_shortest_path(G))

# with open('test.txt', 'w') as a:
#     a.write(str(adjMat))


data_mat_HAL()

teamSize = 5
leastSumDistance = float("-inf")
bestTeam = []
# print adjMat



adjList = {}
