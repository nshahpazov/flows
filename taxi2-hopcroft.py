# taxi problem
MAX_TAXIS = 201
MAX_PEOPLE = 401
N = MAX_TAXIS + MAX_PEOPLE
BLOCK_LENGTH = 200
INFINITY = float("Inf")
NIL = 0

def get_distance(point1, point2):
  return BLOCK_LENGTH * (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def is_reachable(taxi, person, distance):
  return get_distance(taxi, person) <= distance

def fill_network(network, people, taxis, p, t, distance):
  for i in range(p):
    for j in range(t):
      if is_reachable(taxis[j], people[i], distance):
        adjacents[i + 1].append(p+j+1)
        adjacents[p+j+1].append(i + 1)
        network[i][t + j + 1] += 1
        network[t + j + 1][i] += 1

def bfs(graph, matching, n, t):
  queue = []
  for i in range(1, t + 1):
    if not matching[i]:
      distances[i] = 0
      queue.append(i)
    else:
      distances[i] = INFINITY
  distances[NIL] = INFINITY

  while queue:
    left = queue.pop(0)
    if left != NIL:
      for right in adjacents[left]:
        if distances[matching[right]] == INFINITY:
          distances[matching[right]] = distances[left] + 1
          queue.append(matching[right])

  return distances[NIL] != INFINITY

def dfs(graph, matching, left):
  # reverse that returning
  if left != NIL:
    for right in adjacents[left]:
      is_next = distances[matching[right]] == distances[left] + 1
      if is_next and dfs(graph, matching, matching[right]):
        matching[right] = left
        matching[left] = right
        return True
    distances[left] = INFINITY
    return False
  return True

def hopcroft(graph, n, t):
  matching = [NIL] * n
  m = 0
  while bfs(graph, matching, n, t):
    for i in range(1, t+1):
      if matching[i] == NIL and dfs(network, matching, i):
        m += 1
  return m

k = int(raw_input())
for i in range(0, k):
  people = [None] * MAX_PEOPLE
  taxis =  [None] * MAX_TAXIS
  network = [[0] * N for i in range(0, N)]
  adjacents = [[] for i in range(N + 20)]
  distances = [0] * (N)

  p, t, s, c = map(int, raw_input().split())
  n = (p + t + 2)

  for j in range(p):
    x, y = map(int, raw_input().split())
    people[j] = [x, y]
  for j in range(t):
    x, y = map(int, raw_input().split())
    taxis[j] = [x, y]

  fill_network(network, people, taxis, p, t, s * c)
  print hopcroft(network, n, t)
