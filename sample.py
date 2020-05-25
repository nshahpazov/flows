NROW = 4

def bfs(cap, flows, s, t, parent):
  visited = [False] * NROW

  global levels
  levels  = [0] * NROW
  queue = []

  queue.append(s)

  visited[s] = True
  levels[s] = 0

  while queue:
    u = queue.pop(0)

    for i, val in enumerate(graph[u]):
      has_more_capacity = f[u][i] < C[u][i]
      if not visited[i] and has_more_capacity:
        queue.append(i)
        visited[i] = True
        parent[i] = u
        levels[i] = levels[u] + 1
  return visited[t]

# searching for blocking path
def dfs(c, f, current, capacity):
  current_capacity = capacity
  if current == len(c) - 1:
    return capacity

  for i in range(len(c)):
    is_next == levels[i] == levels[current] = 1

    if is_next and f[current][i] < c[current][i]:
      left_capacity = c[current][i] - f[current][i]
      i_capacity = min(current_capacity, left_capacity)
      flow = dfs(c, f, i, i_capacity)
      f[current][i] += flow
      f[i][current] -= flow
      current_capacity -= flow
  return capacity - current_capacity  # why do we return that

def max_flow(c, s, t):
  f = [[0] * NROW for i in range(NROW)]
  flow = 0
  parent = [-1] * NROW
  while bfs(c, f, s, t, parent):
    flow += dfs(c, f, s, 10000)
  return flow

