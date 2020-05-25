MAX_TAXIS = 200
MAX_PEOPLE = 400
BLOCK_LENGTH = 200

# create graph
people = [None] * MAX_PEOPLE
taxis =  [None] * MAX_TAXIS

def dist(point1, point2):
  return BLOCK_LENGTH * (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def is_reachable(taxi, person, taxi_speed, waiting_time):
  res = dist(taxi, person) / taxi_speed <= waiting_time
  return res

def fill_network(network, people, taxis, p, t, s, c):
  for i in range(0, t):
    network[0][i+1] = 1
  for i in range(0, p):
    network[t + i][p + t + 1] = 1

  for i in range(1, t):
    for j in range(0, p):
      # calculate whether i-th taxi has access to jth person and
      # update the network for that taxi -> person
      network[i][t + j + 1] += is_reachable(taxis[i-1], people[j], s, c)


# build level graph by bfs
def bfs(capacities, flows, s, t, n):
  visited = [False] * n
  # not sure if this will be changed
  global levels
  levels = [0] * n
  queue = []
  queue.append(s)
  visited[s] = True
  levels[s] = 0

  while queue:
    current = queue.pop(0)
    for neighbour in range(n):
      has_more_capacity = flows[current][neighbour] < capacities[current][neighbour]
      if not visited[neighbour] and has_more_capacity:
        queue.append(neighbour)
        visited[neighbour] = True
        levels[neighbour] = levels[current] + 1
  return visited[t]

# use dfs for finding blocking flow
def dfs(c, f, current, sink, capacity_so_far, n):
  tmp = capacity_so_far
  if current == n - 1: # we are at the end so return the bn o
    return capacity_so_far

  for i in range(n):
    is_next = levels[i] == levels[current] + 1
    residual_capacity = c[current][i] - f[current][i]
    has_more_capacity = residual_capacity > 0
    if is_next and has_more_capacity:
      min_capacity = min(capacity_so_far, residual_capacity)
      bottleneck = dfs(c, f, i, sink, min_capacity, n)
      if bottleneck > 0:
        f[current][i] += bottleneck
        f[i][current] -= bottleneck
        return bottleneck
  return 0

# dinic's algorithm
def max_flow(capacities_graph, source, sink, n):
  flows_graph = [[0] * n for i in range(n)]
  flow = 0

  while bfs(capacities_graph, flows_graph, source, sink, n):
    flow += dfs(capacities_graph, flows_graph, source, sink, float("Inf"), n)
  return flow

# read input and execute
k = int(raw_input())
for i in range(0, k):
  p, t, s, c = map(int, raw_input().split())
  n = (p + t + 2)
  network = [[0] * n for i in range(0, n)]
  for j in range(0, p):
    x, y = map(int, raw_input().split())
    people[j] = [x, y]
  for j in range(0, t):
    x, y = map(int, raw_input().split())
    taxis[j] = [x, y]

  fill_network(network, people, taxis, p, t, s, c)
  res = max_flow(network, 0, p + t + 1, n)
  print res