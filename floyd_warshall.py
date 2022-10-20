# Compute all pairs shortest path using Floyd-Warshall algorithm


# Implement a graph using adjacency matrix
import numpy as np
class Graph:
    def __init__(self, num_nodes, edges, directed = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.edges = [[(0, 0) for _ in range(num_nodes)]
                                    for _ in range(num_nodes)]
        for (v1, v2, w) in edges:
            self.edges[v1][v2] = (1, w)
            if not self.directed:
                self.edges[v2][v1] = (1, w)
    
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
    
    def __str__(self):
        return (self.__repr__())


# Implement Floyd-Warshall Algorithm
def floyd_warshall(graph):
    # Initialise a three-dimensional (n x n) x (n + 1) matrix
    shortest_path = np.zeros(shape = (graph.num_nodes + 1, graph.num_nodes, graph.num_nodes))
    
    # Set all distances in the first copy of the n x n matrix to infinity 
    for node in range(graph.num_nodes):
        for neighbor in range(graph.num_nodes):
            shortest_path[0, node, neighbor] = np.inf
    
    # Set up the SP-0 matrix (it's just the adjacency matrix of the graph)
    # Just need to place the corresponding weights for all edges in the graph
    for node in range(graph.num_nodes):
        for neighbor in range(graph.num_nodes):
            if graph.edges[node][neighbor][0] == 1:
                shortest_path[0, node, neighbor] = graph.edges[node][neighbor][1]
    
    # Update shortest path of k'th level by comparing distances of (shortest_path using vertex k and without using vertex k) at the (k-1)th level
    # Iterate n + 1 times
    for k in range(1, graph.num_nodes + 1):
        for node in range(graph.num_nodes):
            for neighbor in range(graph.num_nodes):
                shortest_path[k, node, neighbor] = min(shortest_path[k-1, node, neighbor], shortest_path[k-1, node, k-1] + shortest_path[k-1, k-1, neighbor])
    # Return the last copy of the n x n matrix (that's the copy with transitive closure/shortest path fully updated)
    return (shortest_path[graph.num_nodes,:,:])

# Tested using the below graph
# num_nodes = 8
# edges = [(0, 1, 10), (0, 7, 8), (1, 5, 2), (2, 1, 1), (2, 3, 1), (3, 4, 3), (4, 5, -1), (5, 2, -2), (6, 1, -4), (6, 5, -1), (7, 6, 1)]
# graph16 = Graph(num_nodes, edges, directed = True)
# floyd_warshall(graph16)
