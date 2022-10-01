# Implement a graph using adjacency matrix and adjacency list
# Implment the adjacency matrix using both lists and np.zeros 
# Implment adjacency lists using both lists and dictionary


# 1. Undirected, unweighted graph

# Adjacency list using lists
class Graph_adj_list_using_lists:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for e1, e2 in edges:
            self.edges[e1].append(e2)
            self.edges[e2].append(e1)
    
    def __repr__(self):
        return('\n'.join([f'{node}: {neighbor}' for node, neighbor in enumerate(self.edges)]))
    
    def __str(self):
        return self.__repr_()



# Adjacency matrix using lists
class Graph_adj_matrix_using_lists:
    def __init__(self, num_nodes, edges):
        self.num_modes = num_nodes
        self.edges = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        for e1, e2 in edges:
            self.edges[e1][e2] = 1
            self.edges[e2][e1] = 1
    
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for node, neighbor in enumerate(self.edges)]))
    def __str__(self):
        return self.__repr__()



# Adjacency lists using dictionary
class Graph_adj_list_using_dictionary:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.graph_details = {}
        for e1,e2 in edges:
            if e1 in self.graph_details.keys():
                self.graph_details[e1].append(e2)
            else:
                self.graph_details[e1] = [e2]
            if e2 in self.graph_details.keys():
                self.graph_details[e2].append(e1)
            else:
                self.graph_details[e2] = [e1]
    
    def __repr__(self):
        return('\n'.join([f'{node}:{neighbor}' for node, neighbor in self.graph_details.items()]))
    
    def __str__(self):
        return self.__repr__()


# Adjacency lists using dictionary - better implementation for the lazily inclined
class Graph_adj_list_using_dictionary2:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.graph_details = {}
        for i in range(num_nodes):
            self.graph_details[i] = []
        
        for e1, e2 in edges:
            self.graph_details[e1].append(e2)
            self.graph_details[e2].append(e1)
    
    def __repr__(self):
        return('\n'.join([f'{node}:{neighbor}' for node, neighbor in self.graph_details.items()]))
    
    def __str__(self):
        return self.__repr__()


# Adjacency matrix using np.zeros
import numpy as np
class Graph_adj_matrix_using_numpy_zeros:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.graph_details = np.zeros(shape = (num_nodes, num_nodes), dtype = int)
        for (e1, e2) in edges:
            self.graph_details[e1][e2] = 1
            self.graph_details[e2][e1] = 1
    
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for node, neighbor in enumerate(self.graph_details)]))
    
    def __str__(self):
        return self.__repr__()


# 2. Directed, weighted Graphs and everything in between

# Using lists
class Graph_directed_weighted:
    '''Will implement any or all combinations of the following graphs using lists: weighted, unweighted, directed, undirected.'''
    def __init__(self, num_nodes, edges, weighted = False, directed = False):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed
        self.edges = [[] for _ in range(num_nodes)]
        if self.weighted:
            self.weights = [[] for _ in range(num_nodes)]
            for (e1, e2, w) in edges:
                self.edges[e1].append(e2)
                self.weights[e1].append(w)
                if not self.directed:
                    self.edges[e2].append(e1)
                    self.weights[e2].append(w)
        elif not self.weighted:
            for (e1, e2) in edges:
                self.edges[e1].append(e2)
                if not self.directed:
                    self.edges[e2].append(e1)
    
    def __repr__(self):
        if self.weighted:
            return('\n'.join([f'{node}: {list(zip(neighbor, weight))}' for node, (neighbor, weight) in enumerate(zip(self.edges, self.weights))]))
        else:
            return ('\n'.join([f'{node}: {neighbor}' for node, neighbor in enumerate(self.edges)]))
    
    def __str__(self):
        return self.__repr__()
     


# Adjacency list using lists
# num_nodes = 6
# edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
# print("-----------------Adjacency List using Lists------------------")
# graph1 = Graph_adj_list_using_lists(num_nodes, edges)
# print(graph1)


# Adjacency matrix using lists
# num_nodes = 6
# edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
# print("-----------------Adjacency matrix using Lists------------------")
# graph1 = Graph_adj_matrix_using_lists(num_nodes, edges)
# print(graph1)


# Adjacency list using dictionary
# num_nodes = 6
# edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
# print("-----------------Adjacency List using Dictionary------------------")
# graph1 = Graph_adj_list_using_dictionary(num_nodes, edges)
# print(graph1)
# print(graph1.graph_details)


# Adjacency list using dictionary - compact
# num_nodes = 6
# edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
# print("-----------------Adjacency List using Dictionary: compact------------------")
# graph1 = Graph_adj_list_using_dictionary2(num_nodes, edges)
# print(graph1)
# print(graph1.graph_details)


# Adjacency matrix using np.zeros
# num_nodes = 6
# edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
# print("-----------------Adjacency MAtrix using np.zeros------------------")
# graph1 = Graph_adj_matrix_using_numpy_zeros(num_nodes, edges)
# print(graph1)
# print(graph1.graph_details)


# Directed, weighted graphs and everything in between
# Directed and weighted
# num_nodes7 = 5
# edges7 = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (2, 4, 6), (4, 2, 7), (3, 0, 8)]
# graph4 = Graph_directed_weighted(num_nodes7, edges7, directed = True, weighted = True)
# print(f'edges: {graph4.edges}, weights: {graph4.weights}')
# print("-----------------Directed, Weighted Graphs and Everything in Between------------------")
# print(graph4)


# Undirected and weighted graphs
num_nodes7 = 5
edges7 = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (2, 4, 6), (4, 2, 7), (3, 0, 8)]
graph4 = Graph_directed_weighted(num_nodes7, edges7, directed = False, weighted = True)
print(f'edges: {graph4.edges}, weights: {graph4.weights}')
print("-----------------Directed, Weighted Graphs and Everything in Between------------------")
print(graph4)
