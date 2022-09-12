# DFS  - detect cycle


# Implement a graph using adjacency list
class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)
        
    def __repr__(self):
        return ('\n'.join([f'{node}:{neighbor}' for node, neighbor in enumerate(self.edges)]))
    
    def __str__(self):
        return self.__repr__()

# Define a function to detect cycle in a given graph and a root node
def detect_cycle(graph, root):
    '''
    Will return the node containing a cycle if a cycle exists in the graph, otherwise will return 'Acyclic graph'.
    '''
    # Create an empty stack
    stack = []

    # Track visited nodes
    visited = [False] * graph.num_nodes

    # Track the order of traversal
    traversal = []

    # Track the parent of the visited nodes
    parent = [None] * graph.num_nodes

    # Begin traversal
    stack.append(root)
    parent[root] = root

    while len(stack) > 0:
        # Pop the stack
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            traversal.append(node)
            # Check the neighbors for visited nodes, or continue traversal
            for neighbor in graph.edges[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    parent[neighbor] = node

                # If the neighbor is visited, check for back edge 
                # If a back edge exists, neighbor will have been visited before 
                # the parent of the current node
                elif traversal.index(neighbor) < traversal.index(parent[node]):
                    return (f'Cycle at node {node}.')
    return ('Acyclic graph!')

# Setting up the graph and calling the function
num_nodes = 5
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (3, 4)]
graph1 = Graph(num_nodes, edges)
print(graph1)
print(detect_cycle(graph1, 4))
