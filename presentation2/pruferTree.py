import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations


def get_tree(S):
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

# Add edges between 2 vertices that were previously unconnected until the number of edges = num_edges


def add_edges(num_vertices, number_of_edges, edges_arr):
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
    print("Initial Array: ", edges_arr)
    i = 0
    while i < remaining_num_edges:
        print("Possible edges: ", possible_edges)
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
        possible_edges = [t for t in possible_edges if t !=
                          random_edge]
        print("Random edge: ", random_edge)
        i += 1

    print("edges_arr: ", edges_arr, " Length: ", len(edges_arr))
    print()
    return edges_arr


# Generating the graphs with different number of trees
n = 5  # K_n with n vertices
N = 25  # Generate 25 random trees with 20 vertices (as spanning trees of K20)

all_trees = []
for i in range(N):
    S = np.random.choice(range(1, n + 1), n - 2, replace=True).tolist()
    T_E = get_tree(S)  # The spanning tree corresponding to S
    G = add_edges(n, 10, T_E)

    # Create a graph and add edges from the spanning tree
    G = nx.Graph()
    # Adding random weights to the edges
    for edges in T_E:
        G.add_edge(*edges, weights=random.randint(1, 5))

    # G.add_edges_from(T_E)
    all_trees.append(G)

for tree in all_trees:
    # Visualize the spanning tree
    labels = nx.get_edge_attributes(tree, 'weights')
    pos = nx.spring_layout(tree)
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=labels)
    nx.draw(tree, pos, with_labels=True, node_size=200,
            node_color='skyblue', font_size=8)
    plt.title(f"Spanning Tree {i + 1}")
    plt.show()
