from collections import deque

graph = {
    'a': ['b', 'e', 'p'],
    'b': ['c', 'e', 'd'],
    'p': ['d']
}

def bfs(graph,start):
    queue = deque(start)
    visited = deque(start)
    while queue:
        s = queue.popleft()
        if graph.get(s) is not None:
            for i in graph[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
    return visited

def dfs(graph,start):
    visited = deque(start)


print(bfs(graph,'a'))