import sys
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn import metrics
sys.path.insert(0, r'C:\Users\soumy\Desktop\SML\intelligent-team-building-recommendation-system-master\intelligent-team-building-recommendation-system-master')
import constants
sys.path.insert(0, r'C:\Users\soumy\Desktop\SML\intelligent-team-building-recommendation-system-master\intelligent-team-building-recommendation-system-master\parser')
import GetSimilarityMatrix


collaboration_weight = constants.collaborate_weight
author_collab_clean = os.path.join(constants.DATA_PATH,'networks\\author_collaboration_network_clean.txt')

def buildGraph():
    number_authors, authorarray, authormap = GetSimilarityMatrix.getAuthorIDNameMap()
    authorcollabmap = GetSimilarityMatrix.updateSimilarityMatrix(author_collab_clean, authormap, authorarray, collaboration_weight)

    G = nx.Graph()
    count = 0
    for k, v in authorcollabmap.items():
        if count > 300:
            break
        G.add_node(k)
        for node in v:
            for n, w in v.items():
                G.add_edge(k,n, weight=1/w);
        count = count + 1


    return G




def specclustering():
    np.random.seed(1)

    # Get your mentioned graph
    G = buildGraph()

    fileid = open('Graph.txt', 'w')
    for n, nbrs in G.adjacency_iter():
        for nbr, eattr in nbrs.items():
            data = eattr['weight']
            fileid.write('(%d, %d, %f)\n' % (n, nbr, data))

    fileid.close()


    # Get adjacency-matrix as numpy-array
    adj_mat = nx.adjacency_matrix(G)
    print(adj_mat)

    # Cluster
    sc = SpectralClustering(30, affinity='precomputed', n_neighbors=10, n_init=10)
    sc.fit(adj_mat)
    #
    # Compare ground-truth and clustering-results
    print('spectral clustering')
    clusterfile = open('Cluster.txt', 'w')
    i = 0
    while i<len(G.nodes()):
         clusterfile.write('%d ==> %d\n' % (G.nodes()[i], sc.labels_[i]))
         i = i+1

    clusterfile.close()
    pass

if __name__ == "__main__": specclustering()