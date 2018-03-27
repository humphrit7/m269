from graph import Graph

# Your code will be tested on the empty graph and the following graphs

power_grid = Graph()
power_grid.add_edge(1, 2, 100)
power_grid.add_edge(2, 3, 100)
power_grid.add_edge(3, 4, 50)
power_grid.add_edge(3, 5, 50)
power_grid.add_edge(6, 2, 50)
power_grid.add_edge(6, 7, 50)
power_grid.add_edge(7, 8, 40)
power_grid.add_edge(8, 9, 10)
power_grid.add_edge(8, 10, 10)
power_grid.add_edge(8, 11, 20)

single_node = Graph()
single_node.add_node(1)

disconnected = Graph()
disconnected.add_node(1)
disconnected.add_edge(2, 3)

def is_connected(the_graph):
    """Return True if the_graph is connected, otherwise False.

    An empty graph is connected.
    """
    nodes = []
    for node in the_graph.nodes():
        nodes.append(node)
    if len(nodes) == 0:
        return True
    breadth_first_search = the_graph.visited_bfs(nodes[0])
    if len(breadth_first_search) != len(nodes):
        return False
    return True


def disconnection_nodes(graph):
    """Compute the nodes that lead to a disconnected graph.

    After removing any one of the nodes, the graph is disconnected.
    """
    # you must use the `is_connected` function somewhere in your code
    # you can return a set or a list
    disconnects = set()
    edges = graph.weighted_edges()
    for node in graph.nodes():
        graph.remove_node(node)
        if not is_connected(graph):
            disconnects.add(node)
        graph.add_node(node)
        for edge in edges:
            if node in edge[0:2]:
                graph.add_edge(edge[0], edge[1], edge[2])
    return disconnects





print(is_connected(power_grid))
print(is_connected(Graph()))
print(is_connected(single_node))
print(is_connected(disconnected))


the_graph = power_grid
nodes = the_graph.nodes()
print(the_graph._nodes)
edges = the_graph.weighted_edges()
print(the_graph._edges)
print(sorted(disconnection_nodes(the_graph)))
print(nodes == the_graph.nodes())
print(edges == the_graph.weighted_edges())

the_graph = Graph()
nodes = the_graph.nodes()
edges = the_graph.weighted_edges()
print(sorted(disconnection_nodes(the_graph)))
print(nodes == the_graph.nodes())
print(edges == the_graph.weighted_edges())

the_graph = single_node
nodes = the_graph.nodes()
edges = the_graph.weighted_edges()
print(sorted(disconnection_nodes(the_graph)))
print(nodes == the_graph.nodes())
print(edges == the_graph.weighted_edges())

the_graph = disconnected
nodes = the_graph.nodes()
edges = the_graph.weighted_edges()
print(sorted(disconnection_nodes(the_graph)))
print(nodes == the_graph.nodes())
print(edges == the_graph.weighted_edges())