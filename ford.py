from collections import defaultdict
from copy import copy, deepcopy

NROW = 6
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

def bfs(graph, s, t):
  path = []
  # mark all vertices as not visited
  visited = [False] * NROW
  queue = []

  # mark the source node as visited and enqueue it
  queue.append(s)
  visited[s] = True

  while queue:
    u = queue.pop(0)
    path.append(u)
    for ind, val in enumerate(graph[u]):
      if visited[ind] == False and val > 0:
        queue.append(ind)
        visited[ind] = True

  path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
  return path_edges if visited[t] else None

def update_path(graph, path, val):
  for s, v in path:
    graph[s][v] -= val
    graph[v][s] += val

def bottleneck(path, graph):
  return min([graph[i][j] for i, j in path])

def f(s, t):
  path = bfs(graph, s, t)
  max_flow = 0
  while path != None:
    bn = bottleneck(path, graph)
    max_flow += bn
    update_path(graph, path, bn)
    path = bfs(graph, s, t)

  return max_flow
print f(0, 5)