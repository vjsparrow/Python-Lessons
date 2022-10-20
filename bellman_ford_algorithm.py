# Cumpute single source shortest paths in a graph with negative weights using the Bellman-Ford Algorithm


# Implement a graph using adjacency lists
import numpy as np
class Graph:
    def __init__(self, num_nodes, edges, directed = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.edges = [[] for _ in range(num_nodes)]
        for (v1, v2, w) in edges:
            self.edges[v1].append((v2, w))
            if not self.directed:
                self.edges[v2].append((v1, w))

    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
    
    def __str__(self):
        return (self.__repr__())
 

# Cumpute the single source shortest path using Bellman-Ford algorithm
def bellman_ford(graph, root):
    # Set distance of all vertices to infinity
    distance = {}
    for i in range(graph.num_nodes):
        distance[i] = np.inf
    
    # Begin traversal by marking the distance of the root vertex to 0
    distance[root] = 0
    
    # Perform (num_nodes - 1) iterations and update distances of all neighbors in each iteration
    for _ in range(graph.num_nodes):
        for node in range(graph.num_nodes):
            for (neighbor, weight) in graph.edges[node]:
                distance[neighbor] = min(distance[neighbor], distance[node] + weight)
    
    # Return distance
    return (distance)

# # Tested using the below graph
# num_nodes = 8
# edges = [(0, 1, 10), (0, 7, 8), (1, 5, 2), (2, 1, 1), (2, 3, 1), (3, 4, 3), (4, 5, -1), (5, 2, -2), (6, 1, -4), (6, 5, -1), (7, 6, 1)]
# graph15 = Graph(num_nodes, edges, directed = True)
# bellman_ford(graph15, 0)
