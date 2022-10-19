# Topological sort a Directed Acyclic Graph (DAG)


# Implement a DAG
from collections import deque
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for (v1, v2) in edges:
            self.edges[v1].append(v2)
    
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
    
    def __str__(self):
        return (self.__repr__())

    
# Topological sort
def topological_sort(graph):
    # Initialize indegree for all vertices to 0
    indegree = {}
    sorted_sequence = []
    for i in range(graph.num_nodes):
        indegree[i] = 0
    
    # Compute indegree of all vertices
    for node in range(graph.num_nodes):
        for neighbor in graph.edges[node]:
            indegree[neighbor] += 1
    
    # Initialize a queue to store all vertices with indegree = 0
    zero_indegree_queue = deque()
    for node in range(graph.num_nodes):
        if indegree[node] == 0:
            zero_indegree_queue.append(node)
    
    # Sort the vertices topologically
    while len(zero_indegree_queue) > 0:
        # Pop the queue
        next_vertex = zero_indegree_queue.popleft()
        # Append the vertex to the sorted list
        sorted_sequence.append(next_vertex)
        # Remove it from the DAG
        indegree[next_vertex] -= 1
        # Update indegree of all neighbors of next_vertex
        for neighbor in graph.edges[next_vertex]:
            indegree[neighbor] -= 1
            # If the indegree of any neighbor becomes 0 after the update, append it to the queue
            if indegree[neighbor] == 0:
                zero_indegree_queue.append(neighbor)
    
    # Return the sorted list
    return (sorted_sequence)

# Used the below graph to test the code: all good.
# num_nodes = 8
# edges = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (3, 5), (3, 7), (4, 7), (5, 6), (6, 7)]
# graph12 = Graph(num_nodes, edges)
# topological_sort(graph12)
