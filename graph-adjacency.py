class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, src, dest, dist):
        self.graph[src][dest] = dist

    def get_edge(self, src, dest):
        return self.graph[src][dest]

    def pretty_print(self):
        for row in self.graph:
            print(row)


graph = Graph(8)
graph.add_edge(0, 5, 5)
graph.add_edge(0, 2, 1)
graph.add_edge(0, 7, 3)

graph.pretty_print()
