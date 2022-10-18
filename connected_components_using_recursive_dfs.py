# Find components of a graph using recursive dfs


# Implement a graph
class Graph:
  def __init__(self, num_nodes, edges, directed = False, weighted = False):
    self.num_nodes = num_nodes
    self.weighted = weighted
    self.directed = directed
    self.edges = [[] for _ in range(num_nodes)]
    
    if self.weighted:
      for (v1, v2, w) in edges:
        self.edges[v1].append((v2, w))
        if not self.directed:
          self.edges[v2].append((v1, w))
    elif not self.weighted:
      for (v1, v2) in edges:
        self.edges[v1].append(v2)
        if not self.directed:
          self.edges[v2].append(v1)
  
  def __repr__(self):
    return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
  
  def __str__(self):
    return (self.__repr__())
  

# Traverse the graph

# Initialize the visited dictionary
def dfs_initialize(graph):
  visited = {}
  for i in range(graph.num_nodes):
    visited[i] = False
  return (visited)

# Traverse the graph recursively
def dfs_recursive(graph, visited, root):
  visited[root] = True
  for neighbor in graph.edges[root]:
    if not visited[neighbor]:
      visited = dfs_recursive(graph, visited, neighbor)
  return (visited)


# Count the components of the graph
def components(graph):
  # Assign a default component ID to each vertex
  component = {}
  for i in range(graph.num_nodes):
    component[i] = -1
  
  (current_comp_id, count_of_seen_nodes) = (0, 0)
  while count_of_seen_nodes < graph.num_nodes:
    # Select the next_vertex to begin traversal from
    next_vertex = min([node for node in range(graph.num_nodes)
                                  if component[node] == -1])
    # Call the initialize function to reset visited dictionary so that we only count the nodes visited in one iteration
    visited = dfs_initialize(graph)
    # Traverse the graph starting from next_vertex selected earlier
    visited = dfs_recursive(graph, visited, next_vertex)
    for node in visited:
      if visited[node]:
        # Increment the counter for seen nodes by 1 for each node visited in this iteration
        count_of_seen_nodes += 1
        # Assign the current component ID to each node visited during the traversal in the current iteration
        component[node] = current_comp_id
    # Increment the current component ID by 1 for use in the next iteration of the while loop
    current_comp_id += 1
  return (component)


# Taking it for a spin
# num_nodes = 12
# edges = [(0, 1), (0, 4), (2, 3), (2, 6), (2, 7), (3, 7), (4, 8), (4, 9), (6, 7), (6, 10), (7, 10), (7, 11), (8, 9)]
# graph10 = Graph(num_nodes, edges)
# print(components(graph10))
