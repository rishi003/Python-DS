import sys



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex distance form source: ")
        for node in range(self.V):
            print(node, "t", dist[node])


graph = Graph(9)
print(graph.graph)
