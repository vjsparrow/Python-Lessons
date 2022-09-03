# List all connected components of a graph


# Implement a graph using adjacency lists
class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)
    
    def __repr__(self):
        return('\n'.join([f'node{node}: {neighbor}' for node, neighbor in enumerate(self.edges)]))
    
    def __str__(self):
        return self.__repr__()

    
# Define function to traverse the graph using breadth-first search algorithm
def bfs(graph, root):
    # Create a queue
    queue = []

    # Track whether each node is traversed 
    traversed = [False] * len(graph.edges)

    # Set index to traverse the queue
    indx = 0

    # Begin traversal. Set the root node to 'traversed' and enqueue it.
    traversed[root] = True
    queue.append(root)

    while indx < len(queue):
        # Store the current element and point the index to the next element
        current = queue[indx]
        indx += 1

        # Check whether any neighbor of the current element is not traversed yet
        for neighbor in graph.edges[current]:
            if not traversed[neighbor]:
                # Set the node to 'traversed'
                traversed[neighbor] = True
                # Enqueue it
                queue.append(neighbor)
    return (queue, traversed)


# Create a graph object

# Test case 1: 3 Connected components
num_nodes = 9
edges = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]

# Test Case 2: Whole graph is connected (1 connected component)
# num_nodes = 5
# edges = [(0, 1), (0,4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

graph1 = Graph(num_nodes, edges)

# Traverse the graph using bfs
(traversal, trav_bool) = bfs(graph1, 0)

# Check for connected components and if found any, print it

# Created a connected components list and return it
conn_comp = []

# Append the current traversal list to it (if the entire graph is traversed, it would be appended right here)
conn_comp.append(traversal)


# Check if the entire graph is traversed
if len(traversal) != num_nodes:
    i = 0
    # Get to the next undiscovered node
    while i < len(trav_bool):
        if trav_bool[i] == True:
            i += 1
        else:
            # This is the next undiscovered node. Traverse the graph using bfs with this as the root node.
            root = i
            (traversal, trav_bool) = bfs(graph1, root)
            # Append the new nodes traversed (new connected component) to the conn_comp list
            conn_comp.append(traversal)
print(conn_comp)
