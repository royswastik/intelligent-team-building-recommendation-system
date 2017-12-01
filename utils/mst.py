__author__ = 'Swastik'
import networkx as nx

def get_minimum_mst_tree_size_k(graph, k):
    pass


def get_mst_cost(graph, nodes):
    subGraph = graph.subgraph(nodes)
    mst = nx.minimum_spanning_tree(subGraph)
