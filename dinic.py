# Dinic's Algorithm (not fully understood yet)
INFINITY = float("Inf")
NROW = 6

# build level graph by bfs
def bfs(capacities, flows, s, t):
  visited = [False] * NROW
  # not sure if this will be changed
  global levels
  levels = [0] * NROW
  queue = []
  queue.append(s)
  visited[s] = True
  levels[s] = 0

  while queue:
    current = queue.pop(0)
    for neighbour in range(NROW):
      has_more_capacity = flows[current][neighbour] < capacities[current][neighbour]
      if not visited[neighbour] and has_more_capacity:
        queue.append(neighbour)
        visited[neighbour] = True
        levels[neighbour] = levels[current] + 1
  return visited[t]

# use dfs for finding blocking flow
def dfs(c, f, current, sink, capacity_so_far):
  tmp = capacity_so_far
  if current == NROW - 1: # we are at the end so return the bn o
    return capacity_so_far

  for i in range(NROW):
    is_next = levels[i] == levels[current] + 1
    residual_capacity = c[current][i] - f[current][i]
    has_more_capacity = residual_capacity > 0
    if is_next and has_more_capacity:
      min_capacity = min(capacity_so_far, residual_capacity)
      bottleneck = dfs(c, f, i, sink, min_capacity)
      if bottleneck > 0:
        f[current][i] += bottleneck
        f[i][current] -= bottleneck
        return bottleneck
  return 0

def max_flow(capacities_graph, source, sink):
  flows_graph = [[0] * NROW for i in range(NROW)]
  flow = 0

  while bfs(capacities_graph, flows_graph, source, sink):
    flow += dfs(capacities_graph, flows_graph, source, sink, INFINITY)
  return flow

graph = [[ 0, 3, 3, 0, 0, 0 ],  # s
         [ 0, 0, 2, 3, 0, 0 ],  # o
         [ 0, 0, 0, 0, 2, 0 ],  # p
         [ 0, 0, 0, 0, 4, 2 ],  # q
         [ 0, 0, 0, 0, 0, 2 ],  # r
         [ 0, 0, 0, 0, 0, 3 ]]  # t

source = 0  # A
sink = 5    # F
print "Dinic's Algorithm"
max_flow_value = max_flow(graph, source, sink)
print "max_flow_value is", max_flow_value
