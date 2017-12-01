__author__ = 'Ishita'
import os, sys, inspect
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import operator
import networkx as nx

import itertools
# from author_collab import *
# from author_collab import *
# from author_cite_map import *
from author_collaboration_cite_map import *





def data_mat_HAL(G,nodes):
    adjList = []
    adjMat = dict(nx.all_pairs_dijkstra_path_length(G))
    for node1 in nodes:
        temp=[]

        for node2 in nodes:

            if int(node1) in hash_obj.keys() and int(node2) in hash_obj[int(node1)].keys():
                subdict= (adjMat[int(node1)][int(node2)])
                #print subdict,"--------", adjMat[int(node1)][int(node2)]
                temp.append(subdict)

            else:
                temp.append(1000.0)
                #print node1, "----------", node2, "---------"

        adjList.append(temp)
    return adjList



def hal_clustering(adjList,teamSize,nodes):

    cluster_data = AgglomerativeClustering(5).fit_predict(adjList)  #,linkage="complete"
    resMap={}
    for i in xrange(len(cluster_data)):

        if int(cluster_data[i]) in resMap.keys():

            resMap[int(cluster_data[i])].append(int(nodes[i]))
        else:
            resMap[int(cluster_data[i])]=[int(nodes[i])]

    #print resMap
    final_res=[]
    for i in resMap.iterkeys():
        if(len(resMap[i])>=teamSize and len(resMap[i])<20):
            for j in xrange(teamSize):
                #print resMap[i][j]
                final_res.append(resMap[i][j])

    return final_res[:4]
# hal_clustering()