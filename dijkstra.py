from collections import deque

graph = {
    'start': {
        'a': 10,
        'b': 5
    },
    'b': {
        'a': 2,
        'fin': 6
    },
    'a': {
        'fin': 1
    },
    'fin': {}
}


def shortest_path(graph, start, end, visited=[], distances={}, parents={}):
    if start not in graph:
        raise TypeError("starting point not in the graph")
    if end not in graph:
        raise TypeError("Ending point not in graph")

    if start == end:
        path = []
        pred = end
        while pred != None:
            path.append(pred)
            pred = parents.get(pred, None)
        readable = path[0]
        for index in range(1, len(path)): readable = path[index] + ' -> ' + readable
        print(readable, distances[end])
    else:
        if not visited:
            distances[start] = 0
        for neighbor in graph[start]:
            if neighbor not in visited:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    parents[neighbor] = start
        visited.append(start)
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        shortest_path(graph, x, end, visited, distances, parents)


shortest_path(graph, 'start', 'fin')
