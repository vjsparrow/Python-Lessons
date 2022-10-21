# Find a Minimum Cost Spanning Tree in a weighted graph using the Prim's Algorithm


# Implement a graph using adjacency list
import numpy as np
class Graph:
    def __init__(self, num_nodes, edges, directed = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.edges = [[] for _ in range(num_nodes)]

        for (v1, v2, weight) in edges:
            self.edges[v1].append((v2, weight))
            if not self.directed:
                self.edges[v2].append((v1, weight))
    
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
    
    def __str__(self):
        return (self.__repr__())


# Prim's Algorithm
def prims_algorithm(graph):
    # Initialize visited to False, distance to infinity and neighbor_of to -1 for all vertices
    (visited, distance, neighbor_of) = ({}, {}, {})
    for i in range(graph.num_nodes):
        (visited[i], distance[i], neighbor_of[i]) = (False, np.inf, -1)
    # Add node 0 to the graph by marking it visited
    visited[0] = True
    # Update the distance and neighbor_of of all neighbors of node 0
    for (neighbor, weight) in graph.edges[0]:
        distance[neighbor] = weight
        neighbor_of[neighbor] = 0
    # Iterate n - 1 times to add the remaining (n-1) vertices to the mcst
    for _ in range(graph.num_nodes - 1):
        # In each iteration, find the minimum distance for all unvisited nodes
        min_dist = min([distance[node] for node in range(graph.num_nodes)
                                            if not visited[node]])
        # Find the unvisited node(s) located at this minimum distance
        next_vertices_list = [node for node in range(graph.num_nodes)
                                        if not visited[node] and 
                                            distance[node] == min_dist]
        # Cover the edge case in case the graph is not connected
        if next_vertices_list == []:
            break
        # From the list of nodes located at minimum distance, pick one as the next vertex
        next_vertex = min(next_vertices_list)
        # Mark the next vertex visited
        visited[next_vertex] = True
        # Update distance and neighbor_of of all unvisited neighbors of the next vertex
        for (neighbor, weight) in graph.edges[next_vertex]:
            if not visited[neighbor]:
                distance[neighbor] = min(distance[neighbor], weight)
                neighbor_of[neighbor] = next_vertex
    # Return the neighbor_of dictionary
    return (neighbor_of)
        
