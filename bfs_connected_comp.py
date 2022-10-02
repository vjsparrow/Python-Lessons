# Find the connected components of a graph using BFS


# Implement the graph
class Graph_adj_list:
    def __init__(self, num_nodes, edges, directed = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.edges = [[] for _ in range(num_nodes)]
        for (e1, e2) in edges:
            self.edges[e1].append(e2)
            if not self.directed:
                self.edges[e2].append(e1)
    
    def __repr__(self):
        return('\n'.join([f'{node}: {neighbor}' for node, neighbor in enumerate(self.edges)]))
    
    def __str__(self):
        return self.__repr__()


# Traverse the graph using BFS and return the visited status
def bfs(graph, root):
    # Implement a queue
    from collections import deque
    queue = deque()
    
    # Track visited items
    visited = [False] * graph.num_nodes

    # Begin traversal
    queue.append(root)
    visited[root] = True

    while len(queue) > 0:
        # Extract the leftmost element of the queue
        node = queue.popleft()

        # Explore all unvisited neighbors of the current node and add them to the queue
        for neighbor in graph.edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return visited


# Find the number of connected components
def connected_components(graph):
    components = {}
    for i in range(graph.num_nodes):
        components[i] = -1
    
    (current_comp_id, count_of_seen_nodes) = (0, 0)

    while count_of_seen_nodes < graph.num_nodes:
        root = min([node for node in range(graph.num_nodes) if components[node] == -1])
        visited_nodes = bfs(graph, root)
        for node in range(len(visited_nodes)):
            if visited_nodes[node]:
                components[node] = current_comp_id
                count_of_seen_nodes += 1
        current_comp_id += 1
    
    return (components)


# Creating graph objects and calling the functions

num_nodes = 6
edges = [(0, 1), (0, 3), (0, 4), (1, 5), (2, 3), (2, 5), (4, 5)]
print("-----------------Adjacency List using Lists------------------")
graph1 = Graph_adj_list(num_nodes, edges)
print(graph1)
print(graph1.edges)
print(connected_components(graph1))
