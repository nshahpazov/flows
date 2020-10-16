INFINITY = float("Inf")

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

t = (2 * n) + 2

# prepare network
network = [[0] * t for i in range(t)]
pushed = [[0] * t for i in range(t)]
for i in range(1, n + 1):
  network[0][i] = a[i - 1]
  network[n + i][t - 1] = b[i-1]

  network[i][n + i] = INFINITY

for k in range(m):
  i, j = map(int, raw_input().split())
  network[i][n + j] = INFINITY
  network[j][n + i] = INFINITY

# algorithm
def bfs(graph, s, t, parent, n):
  visited  = [False] * n
  queue = []

  queue.append(s)
  visited[s] = True

  while queue:
    u = queue.pop(0)

    for i, edge in enumerate(graph[u]):
      if not visited[i] and edge > 0:
        queue.append(i)
        visited[i] = True
        parent[i] = u
  return visited[t]

def ford_fulkerson(graph, n, source, sink):
  parent = [-1] * n

  max_flow = 0

  while bfs(graph, source, sink, parent, n):
    # calculate residual capacity on that path
    path_flow = INFINITY
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
      graph
      if u < n/2:
        pushed[u][v] += path_flow
      else:
        pushed[u][v] -= path_flow
      v = parent[v]
  return max_flow

res = ford_fulkerson(network, t, 0, t - 1)
if res == sum(a) and res == sum(b):
  print "YES"
  for i in range(1, n+1):
    print ' '.join([str(i) for i in pushed[i][(n+1):t-1]])
else:
  print "NO"
