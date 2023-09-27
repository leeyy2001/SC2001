import sys


def dijkstra(graph, start):
    # Initialize the distance list with infinite values for all nodes except the start node
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0

    # Create a set to keep track of visited nodes
    visited = set()

    while len(visited) < n:
        # Find the node with the minimum distance that has not been visited
        min_distance = float('inf')
        min_node = None
        for v in range(n):
            if distance[v] < min_distance and v not in visited:
                min_distance = distance[v]
                min_node = v

        if min_node is None:
            break

        # Mark the minimum distance node as visited
        visited.add(min_node)

        # Update the distances for adjacent nodes
        for v in range(n):
            if graph[min_node][v] != 32767 and v not in visited:
                new_distance = distance[min_node] + graph[min_node][v]
                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


# Given adjacency matrix
adjacency_matrix = [
    [0, 5, 1, 5, 32767],
    [5, 0, 5, 32767, 3],
    [1, 5, 0, 32767, 2],
    [5, 32767, 32767, 0, 2],
    [32767, 3, 2, 2, 0]
]

start_node = 0  # You can change this to the desired starting node

shortest_distances = dijkstra(adjacency_matrix, start_node)
print("Shortest distances from node {}:".format(start_node))
for i, distance in enumerate(shortest_distances):
    print("Node {}: {}".format(i, distance))


# Given adjacency list
adjacency_list = {
    1: [[2, 3], [4, 4], [3, 3]],
    2: [[1, 3], [5, 1]],
    3: [[1, 3], [4, 2], [5, 4]],
    4: [[1, 4], [3, 2], [5, 4]],
    5: [[2, 1], [4, 4], [3, 4]]
}

num_vertices = len(adjacency_list)
start_node = 1  # Change this to the desired starting node

dijkstra_obj = DijkstraAdjList(num_vertices, adjacency_list)
shortest_distances = dijkstra_obj.dijkstra(start_node)

print("Shortest distances from node", start_node)
for vertex, distance in enumerate(shortest_distances):
    print("To node", vertex + 1, ":", distance)
