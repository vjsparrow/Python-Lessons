# Compute a Minimum Cost Spanning Tree (MCST) in a weighted graph using Kruskal's Algorithm


# Implement a graph using adjacency list
class Graph:
    # Graph constructor
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = [[] for _ in range(num_nodes)]
        for (u, v, w) in edges:
            self.edges[u].append((v, w))
            self.edges[v].append((u, w))
    
    # String representation of the graph
    def __repr__(self):
        return ('\n'.join([f'{node}: {neighbor}' for (node, neighbor) in enumerate(self.edges)]))
    
    def __str__(self):
        return (self.__repr__())

  
# Kruskal's Algorithm
def kruskals_algorithm(graph):
    # Initialize edges and tree_edges as empty lists, and component, members_of_component, and size_of_component as empty dictionaries
    (edges, tree_edges, component, members_of_component, size_of_component) = ([], [], {}, {}, {})
    
    for node in range(graph.num_nodes):
        # Let each vertex be it's own component
        component[node] = node
        # Rearrange the edges in the form (weight, node1, node2)
        edges.extend([(weight, node, neighbor) for (neighbor, weight) in graph.edges[node]])
        # Set each vertex as the only member of it's component
        members_of_component[node] = [node]
        # Set the size of each component block as one
        size_of_component[node] = 1         # Initalization complete
    
    # Sort the edges in ascending order
    edges.sort()

    # For every edge (weight, node, neighbor):
    for (weight, node, neighbor) in edges:
        # If node and neighbor have different component IDs, append the edge to tree_edges
        if component[node] != component[neighbor]:
            tree_edges.append((node, neighbor))
            # Get the component IDs of both vertices in the edge
            component_of_node = component[node]
            component_of_neighbor = component[neighbor]
            # Update the component ID of the smaller block
            if size_of_component[component_of_node] < size_of_component[component_of_neighbor]:
                # For all vertices that have the same component as the node:
                for vertex in members_of_component[component_of_node]:
                    # Change the component ID to that of the neighbor
                    component[vertex] = component_of_neighbor
                    # Make the vertex a member of newly assigned component block
                    members_of_component[component_of_neighbor].append(vertex)
                    # Increment the size of the component block by 1 for each vertex added to the component block
                    size_of_component[component_of_neighbor] += 1
            # If neighbor's component block is smaller than that of the node
            else:
                for vertex in members_of_component[component_of_neighbor]:
                    component[vertex] = component_of_node
                    members_of_component[component_of_node].append(vertex)
                    size_of_component[component_of_node] += 1
            
    # Return tree_edges
    return (tree_edges)


# Tested using this graph:
# num_nodes = 7
# edges = [(0, 1, 10), (0, 2, 18), (1, 2, 6), (1, 4, 20), (2, 3, 70), (4, 5, 10), (4, 6, 10), (5, 6, 5)]
# graph19 = Graph(num_nodes, edges)
# # print(graph18)
# print(kruskals_algorithm(graph19))
