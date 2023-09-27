import sys
from generateGraph import GraphGen
import time

import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from math import comb


class DjikstraAdjMatrix:
    def __init__(self, graph, num_vertices):
        self.V = num_vertices
        # self.graph = [[0 for column in range(num_vertices)]
        #               for row in range(num_vertices)]
        self.graph = graph

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node+1, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        # self.printSolution(dist)


# # The nodes in the algorithm start from 0 and end at V-1
# source = 1  # You can change this to the desired starting node

# time_arr_avg = []
# vertice_arr = []

# bottom_range = 20
# top_range = 100

# for vertices in range(bottom_range, top_range, 1):
#     vertice_arr.append(vertices)

#     time_arr = []
#     for i in range(100):
#         allGraphs = GraphGen(vertices, vertices-1)
#         graph = allGraphs.generateGraph()
#         adjMatrix = allGraphs.testCreateAdjMatrix(graph)

#         djikstra_obj = DjikstraAdjMatrix(adjMatrix, vertices)
#         start = time.perf_counter()
#         djikstra_obj.dijkstra(source-1)
#         end = time.perf_counter()

#         time_arr.append(end-start)

#     time_arr_avg.append(mean(time_arr))


# plt.plot(vertice_arr, time_arr_avg, label="Dijkstra with Adjacency Matrix")
# plt.xlabel('Number of Vertices (V)')
# plt.ylabel('Average CPU Time')
# plt.title('Edges fixed at V-1, Vertices varied')
# plt.grid(True)
# plt.legend()
# plt.show()


# The nodes in the algorithm start from 0 and end at V-1
source = 1  # You can change this to the desired starting node
vertices = 30

time_arr_avg = []
edge_arr = []

for edges in range(vertices-1, comb(vertices, 2) + 1):
    edge_arr.append(edges)

    time_arr = []
    for i in range(20):
        allGraphs = GraphGen(vertices, edges)
        graph = allGraphs.generateGraph()
        adjMatrix = allGraphs.testCreateAdjMatrix(graph)

        djikstra_obj = DjikstraAdjMatrix(adjMatrix, vertices)
        start = time.perf_counter()
        djikstra_obj.dijkstra(source-1)
        end = time.perf_counter()

        time_arr.append(end-start)

    time_arr_avg.append(mean(time_arr))


plt.plot(edge_arr, time_arr_avg, label="Dijkstra with Adjacency Matrix")
plt.xlabel('Number of Edges (E)')
plt.ylabel('Average CPU Time')
plt.title(f'Edges Varied, Vertices Fixed at {vertices}')
plt.grid(True)
plt.legend()
plt.show()
