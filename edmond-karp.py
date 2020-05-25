NROW = 6
graph = [[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

def bfs(s, t, parent):
  visited  = [False] * NROW
  queue = []

  queue.append(s)
  visited[s] = True

  while queue:
    current = queue.pop(0)

    for neighbour, weight in enumerate(graph[current]):
      if not visited[neighbour] and weight > 0:
        queue.append(neighbour)
        visited[neighbour] = True
        parent[neighbour] = current
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

    # update residual graph (augment path)
    v = sink
    while v != source:
      u = parent[v]
      graph[u][v] -= path_flow
      graph[v][u] += path_flow
      v = parent[v]
  return max_flow

res = f(0, 5)
print ("The maximum possible flow is %d " % res)
