import networkx as nx
import random
import numpy as np
from itertools import combinations, groupby
import matplotlib.pyplot as plt


class GraphGen:
    # num_graphs
    def __init__(self, num_vertices, num_edges):
        # The initialization generates a number of graphs, with a specified number of vertices and specified number of edges
        self.num_vertices = num_vertices
        # self.num_graphs = num_graphs

        self.max_num_edges = self.num_vertices * (self.num_vertices - 1)/2
        if (num_edges > self.max_num_edges):
            self.num_edges = self.max_num_edges

        elif (num_edges <= self.max_num_edges):
            self.num_edges = num_edges

        # for i in range(self.num_graphs):
        #     S = np.random.choice(range(1, self.num_vertices + 1),
        #                          self.num_vertices - 2, replace=True).tolist()
        #     T_E = self.get_tree(S)  # The spanning tree corresponding to S
        #     self.G = self.add_edges(self.num_vertices, self.num_edges, T_E)

        #     # Create a graph and add edges from the spanning tree
        #     self.G = nx.Graph()
        #     # Adding random weights to the edges
        #     for edges in T_E:
        #         self.G.add_edge(*edges, weights=random.randint(1, 5))

        #     # G.add_edges_from(T_E)
        #     self.all_trees.append(self.G)

        # return self.all_trees

    def generateGraph(self):
        self.all_trees = []

        S = np.random.choice(range(1, self.num_vertices + 1),
                             self.num_vertices - 2, replace=True).tolist()
        T_E = self.get_tree(S)  # The spanning tree corresponding to S
        self.G = self.add_edges(self.num_vertices, self.num_edges, T_E)

        # Create a graph and add edges from the spanning tree
        self.G = nx.Graph()
        # Adding random weights to the edges
        for edges in T_E:
            self.G.add_edge(*edges, weights=random.randint(1, 5))

        # G.add_edges_from(T_E)
        # self.all_trees.append(self.G)
        return self.G

    # A random graph with different weights each time

    def generate_random_connected_graph(self, n, p):
        """
        Generates a random undirected graph, similarly to an Erdős-Rényi 
        graph, but enforcing that the resulting graph is connected
        """
        edges = combinations(range(n), 2)
        G = nx.Graph()
        G.add_nodes_from(range(n))
        if p <= 0:
            return G
        if p >= 1:
            return nx.complete_graph(n, create_using=G)
        for _, node_edges in groupby(edges, key=lambda x: x[0]):
            node_edges = list(node_edges)
            random_edge = random.choice(node_edges)
            G.add_edge(*random_edge, weights=random.randint(1, 5))
            for e in node_edges:
                if random.random() < p:
                    G.add_edge(*e, weights=random.randint(1, 5))
        return G

    # A graph with fixed number vertices and different number of edges, a number of graphs are generated
    def get_tree(self, S):
        n = len(S)
        L = set(range(1, n + 2 + 1))
        tree_edges = []
        for i in range(n):
            u, v = S[0], min(L - set(S))
            S.pop(0)
            L.remove(v)
            tree_edges.append((u, v))
        tree_edges.append((L.pop(), L.pop()))

        # Returns an array of all connected vertices
        return tree_edges

    # Add edges between 2 vertices that were previously unconnected until the number of edges = self.
    def add_edges(self, num_vertices, number_of_edges, edges_arr):
        remaining_num_edges = number_of_edges - num_vertices + 1
        possible_edges = list(combinations(range(num_vertices), 2))
        possible_edges = [
            (x + 1, y + 1) for x, y in possible_edges]

        # Now we remove edges that are already in the tree
        possible_edges_set = set(possible_edges)
        T_E_set = set(edges_arr)
        common_tuples = possible_edges_set.intersection(T_E_set)
        possible_edges = list(possible_edges_set - common_tuples)

        # Select random edges and keep adding until we hit the number of edges
        # for i in range(remaining_num_edges):
        # print("Initial Array: ", edges_arr)
        i = 0
        while i < remaining_num_edges:
            # print("Possible edges: ", possible_edges)
            random_edge = random.choice(possible_edges)
            # Removal of duplicate edges. Eg. random_edge = (1,3) and (3,1) in possible_edges
            if random_edge in edges_arr or random_edge[::-1] in edges_arr:
                # Remove the tuple or its reversed form from the list
                if random_edge in possible_edges:
                    possible_edges.remove(random_edge)
                else:
                    possible_edges.remove(random_edge[::-1])
                continue

            edges_arr.append(random_edge)
            # Removing appended edge
            possible_edges = [t for t in possible_edges if t !=
                              random_edge]
            # print("Random edge: ", random_edge)
            i += 1

        # print("edges_arr: ", edges_arr, " Length: ", len(edges_arr))
        # print()
        return edges_arr

    # Generate adjacency list
    def createAdjList(self, graph_arr):
        '''
        Input: An array of networkx graph objects

        Output: An array of adjacency lists
        '''
        # return adjacency_arr
        adjacency_arr = []

        for graph in graph_arr:
            adjList = {}
            num_of_nodes = graph.number_of_nodes()
            # Initialize adjList
            for i in range(num_of_nodes):
                adjList[i+1] = []

            for u, v in graph.edges:
                adjList[u].append([v, graph.get_edge_data(u, v)['weights']])
                adjList[v].append([u, graph.get_edge_data(v, u)['weights']])

            adjacency_arr.append(adjList)

        return adjacency_arr

    def testCreateAdjList(self, graph):
        adjList = {}
        num_of_nodes = graph.number_of_nodes()
        # Initialize adjList
        for i in range(num_of_nodes):
            adjList[i+1] = []

        for u, v in graph.edges:
            adjList[u].append([v, graph.get_edge_data(u, v)['weights']])
            adjList[v].append([u, graph.get_edge_data(v, u)['weights']])

        return adjList

    # Generate adjacency matrix

    def createAdjMatrix(self, graph_arr):
        '''
        Input: Networkx Graph object

        Output: An array of adjacency list
        '''
        adj_matrix_list = []

        for graph in graph_arr:
            num_of_nodes = graph.number_of_nodes()
            # Initialise 2D Array
            adj_matrix = np.full(
                shape=(num_of_nodes, num_of_nodes), fill_value=np.iinfo(np.int16).max)
            np.fill_diagonal(adj_matrix, 0)

            for u, v in graph.edges:
                if graph.get_edge_data(u, v) != None:
                    adj_matrix[u-1][v -
                                    1] = graph.get_edge_data(u, v)['weights']
                    adj_matrix[v-1][u-1] = graph.get_edge_data(v, u)['weights']

            adj_matrix_list.append(adj_matrix)

        return adj_matrix_list

    def testCreateAdjMatrix(self, graph):
        num_of_nodes = graph.number_of_nodes()
        # Initialise 2D Array
        adj_matrix = np.full(
            shape=(num_of_nodes, num_of_nodes), fill_value=np.iinfo(np.int16).max)
        np.fill_diagonal(adj_matrix, 0)

        for u, v in graph.edges:
            if graph.get_edge_data(u, v) != None:
                adj_matrix[u-1][v -
                                1] = graph.get_edge_data(u, v)['weights']
                adj_matrix[v-1][u-1] = graph.get_edge_data(v, u)['weights']

        return adj_matrix

    def show_graph(self, graph_arr):
        for id, graph in enumerate(graph_arr):
            # Visualize the spanning tree
            labels = nx.get_edge_attributes(graph, 'weights')
            pos = nx.spring_layout(graph)
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
            nx.draw(graph, pos, with_labels=True, node_size=200,
                    node_color='skyblue', font_size=8)
            plt.title(f"Spanning Tree {id + 1}")
            plt.show()

    def testShowGraph(self, graph):
        print(graph)
        # Visualize the spanning tree
        labels = nx.get_edge_attributes(graph, 'weights')
        pos = nx.spring_layout(graph)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw(graph, pos, with_labels=True, node_size=200,
                node_color='skyblue', font_size=8)
        plt.title(f"Graph")
        plt.show()


# Just generating a random graph
# nodes = random.randint(5, 10)
# nodes = 10
# seed = random.randint(1, 10)
# probability = 0.1
# graphObj = GraphGen()
# G = graphObj.generate_random_connected_graph(nodes, probability)

# plt.figure(figsize=(8, 5))

# labels = nx.get_edge_attributes(G, 'weights')
# pos = nx.spring_layout(G)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# nx.draw(G, pos, node_color='lightblue',
#         with_labels=True,
#         node_size=500)
# plt.show()

# num_vertices = 7
# num_edges = 21

# allGraphs = GraphGen(num_vertices, num_edges)
# graph = allGraphs.generateGraph()

# # Returns an array of adjacency matrices
# adjMatrix = allGraphs.testCreateAdjMatrix(graph)
# print("Adjacency Matrix:")
# print(adjMatrix)
# allGraphs.testShowGraph(graph)

# # Returns an array of adjacency lists
# adjList = allGraphs.createAdjList(graphs)
# print("Adjacency List:")
# for key, val in adjList[0].items():
#     print(key, " -> ", val)
# # print(adjList[0])

# for id, graph in enumerate(graphs):
#     # Visualize the spanning tree
#     labels = nx.get_edge_attributes(graph, 'weights')
#     pos = nx.spring_layout(graph)
#     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
#     nx.draw(graph, pos, with_labels=True, node_size=200,
#             node_color='skyblue', font_size=8)
#     plt.title(f"Spanning Tree {id + 1}")
#     plt.show()
