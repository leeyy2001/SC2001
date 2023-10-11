from collections import defaultdict
import sys

from generateGraph import GraphGen
from djikstraAdjMatrix import DjikstraAdjMatrix
import time
from statistics import mean
import matplotlib.pyplot as plt
from math import comb
from testDijkstra import Graph


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2

        if (left < self.size and
            self.array[left][1]
                < self.array[smallest][1]):
            smallest = left

        if (right < self.size and
            self.array[right][1]
                < self.array[smallest][1]):
            smallest = right

        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:

            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    # Standard function to extract minimum
    # node from heap
    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not heapified. This is a O(Logn) loop
        while (i > 0 and self.array[i][1] <
               self.array[(i - 1) // 2][1]):

            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i-1)//2
            self.pos[self.array[(i-1)//2][0]] = i
            self.swapMinHeapNode(i, (i - 1)//2)

            # move to parent index
            i = (i - 1) // 2

    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(dist, n):
    print("Vertex\tDistance from source")
    for i in range(n):
        print("%d\t\t%d" % (i+1, dist[i]))


class DijkstraAdjList():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):

        # Add an edge from src to dest. A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    # The main function that calculates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src):

        V = self.V  # Get the number of vertices in graph
        dist = []  # dist values used to pick minimum
        # weight edge in cut

        # minHeap represents set E
        minHeap = Heap()

        # Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(V):
            dist.append(1e7)
            minHeap.array.append(minHeap.
                                 newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (minHeap.isInMinHeap(v) and
                        dist[u] != 1e7 and
                        pCrawl[1] + dist[u] < dist[v]):
                    dist[v] = pCrawl[1] + dist[u]

                    # update distance value
                    # in min heap also
                    minHeap.decreaseKey(v, dist[v])

        # printArr(dist, V)


# allGraphs = GraphGen(5, 5, 7)
# graphs = allGraphs.all_trees
# adjList = allGraphs.createAdjList(graphs)

# Initializes a graph of V number of vertices
# graph = DijkstraAdjList(5)
# # node and edge minus 1 as the graph is 0 indexed. Thus starting from node 0 to V-1
# for node, edge_list in adjList[0].items():
#     for dest, weight in edge_list:
#         graph.addEdge(node-1, dest-1, weight)

# source = 1
# print("Dijkstra from adjacency list")
# graph.dijkstra(source-1)

# print("Dijkstra from adjacency matrix")
# adjMatrix = allGraphs.createAdjMatrix(graphs)
# djikstra_obj = DjikstraAdjMatrix(adjMatrix[0], 5)
# djikstra_obj.dijkstra(source-1)

# source = 1

# time_arr_avg_list = []
# time_arr_avg_matrix = []
# vertice_arr = []

# bottom_range = 10
# top_range = 30

# for vertices in range(bottom_range, top_range, 1):
#     vertice_arr.append(vertices)

#     time_arr_list = []
#     time_arr_matrix = []
#     for i in range(100):
#         # Graph creation
#         allGraphs = GraphGen(vertices, ((vertices**2 - vertices)//2) + 5)
#         single_graph = allGraphs.generateGraph()
#         adjList = allGraphs.testCreateAdjList(single_graph)
#         adjMatrix = allGraphs.testCreateAdjMatrix(single_graph)

#         # print(adjMatrix)
#         # print(adjList)

#         # Initializes a graph of V number of vertices
#         graph = DijkstraAdjList(vertices)
#         # node and edge minus 1 as the graph is 0 indexed. Thus starting from node 0 to V-1
#         for node, edge_list in adjList.items():
#             for dest, weight in edge_list:
#                 graph.addEdge(node-1, dest-1, weight)

#         start = time.perf_counter()
#         graph.dijkstra(source-1)
#         end = time.perf_counter()
#         time_arr_list.append(end-start)

#         djikstra_obj = DjikstraAdjMatrix(adjMatrix, vertices)
#         startM = time.perf_counter()
#         djikstra_obj.dijkstra(source-1)
#         endM = time.perf_counter()
#         time_arr_matrix.append(endM-startM)

#     time_arr_avg_list.append(mean(time_arr_list))
#     time_arr_avg_matrix.append(mean(time_arr_matrix))

# plt.plot(vertice_arr, time_arr_avg_list, label="Dijkstra with Adjacency List")
# plt.plot(vertice_arr, time_arr_avg_matrix,
#          label="Dijkstra with Adjacency Matrix")
# plt.xlabel('Number of Vertices (V)')
# plt.ylabel('Average CPU Time')
# plt.title('Edges fixed at V(V-1)/2, Vertices varied')
# plt.grid(True)
# plt.legend()
# plt.show()


# The nodes in the algorithm start from 0 and end at V-1
source = 1  # You can change this to the desired starting node
vertices = 30

time_arr_avg_list = []
time_arr_avg_matrix = []
edge_arr = []

for edges in range(vertices-1, comb(vertices, 2) + 1):
    edge_arr.append(edges)

    time_arr_list = []
    time_arr_matrix = []
    for i in range(30):
        allGraphs = GraphGen(vertices, edges)
        graph = allGraphs.generateGraph()
        adjList = allGraphs.testCreateAdjList(graph)
        adjMatrix = allGraphs.testCreateAdjMatrix(graph)

        # Initializes a graph of V number of vertices
        graph = DijkstraAdjList(vertices)
        # graph = Graph(vertices)
        # node and edge minus 1 as the graph is 0 indexed. Thus starting from node 0 to V-1
        for node, edge_list in adjList.items():
            for dest, weight in edge_list:
                graph.addEdge(node-1, dest-1, weight)

        # djikstra_obj = DijkstraAdjList(vertices)
        start = time.perf_counter()
        graph.dijkstra(source-1)
        # graph.shortestPath(source-1)
        end = time.perf_counter()

        # djikstra_obj = DjikstraAdjMatrix(adjMatrix, vertices)
        djikstra_obj = Graph(vertices)
        djikstra_obj.graph = adjMatrix
        startM = time.perf_counter()
        djikstra_obj.dijkstra(source-1)
        endM = time.perf_counter()

        time_arr_list.append(end-start)
        time_arr_matrix.append(endM - startM)

    time_arr_avg_list.append(mean(time_arr_list))
    time_arr_avg_matrix.append(mean(time_arr_matrix))

plt.plot(edge_arr, time_arr_avg_list, label="Dijkstra with Adjacency List")
plt.plot(edge_arr, time_arr_avg_matrix, label="Dijkstra with Adjacency Matrix")
plt.xlabel('Number of Edges (E)')
plt.ylabel('Average CPU Time')
plt.title(f'Edges Varied, Vertices Fixed at {vertices}')
plt.grid(True)
plt.legend()
plt.show()
