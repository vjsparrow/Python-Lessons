# Compute the longest path in a Directed Acyclic Graph (DAG)


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

  
# Longest path in a DAG
def longest_path(graph):
  # Initialize longest_path and indgree to 0 for all vertices
  (longest_path, indegree) = ({}, {})
  for i in range(graph.num_nodes):
    (longest_path[i], indegree[i]) = (0, 0)
  # Compute indegree of all vertices
  for node in range(graph.num_nodes):
    for neighbor in graph.edges[node]:
      indegree[neighbor] += 1
  # Initialize a queue to store all vertices where indegree[vertices] == 0
  zero_indegree_queue = deque()
  for node in range(graph.num_nodes):
    if indegree[node] == 0:
      zero_indegree_queue.append(node)
  # While the queue is not empty:
  while len(zero_indegree_queue) > 0:
    # Pop the queue and store it in next_vertex
    next_vertex = zero_indegree_queue.popleft()
    # Remove it from the DAG
    indegree[next_vertex] -= 1
    # Update the indegree of all it's neighbors
    for neighbor in graph.edges[next_vertex]:
      indegree[neighbor] -= 1
      # If the indegree of any neighbor of next_vertex becomes zero after the update, append it to the queue
      if indegree[neighbor] == 0:
        zero_indegree_queue.append(neighbor)
      # Update the longest path of all neighbors of next_vertex
      longest_path[neighbor] = max(longest_path[neighbor], longest_path[next_vertex] + 1)
  # Return longest_path
  return (longest_path)

# Tested the code using the below graph
# num_nodes = 8
# edges = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (3, 5), (3, 7), (4, 7), (5, 6), (6, 7)]
# graph1 = Graph(num_nodes, edges)
# longest_path(graph1)
