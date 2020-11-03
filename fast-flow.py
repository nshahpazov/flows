from copy import copy, deepcopy

# read n and m
n, m = map(int, raw_input().split())

# create graph
graph = [ [ 0 for i in range(n) ] for j in range(n) ]
NROW = n

# read lines
for k in range(1, m):
  i, j, capacity = map(int, raw_input().split())
  if  i == j:
    continue
  graph[i-1][j-1] += capacity
  graph[j-1][i-1] += capacity

def bfs(s, t, parent):
  visited  = [False] * NROW
  queue = []

  queue.append(s)
  visited[s] = True

  while queue:
    u = queue.pop(0)

    for i, val in enumerate(graph[u]):
      if visited[i] == False and val > 0:
        queue.append(i)
        visited[i] = True
        parent[i] = u

  return visited[t]

def f(source, sink):
  parent = [-1] * NROW
  max_flow = 0

  while bfs(source, sink, parent):
    # calculate residual capacity on that path
    path_flow = float("Inf")
    s = sink
    while s != source:
      path_flow = min(path_flow, graph[parent[s]][s])
      s = parent[s]

    max_flow += path_flow

    # update residual graph
    v = sink
    while v != source:
      u = parent[v]
      graph[u][v] -= path_flow
      graph[v][u] += path_flow
      v = parent[v]
  return max_flow

result = max_flow(graph, 0, n - 1)
print(result)
