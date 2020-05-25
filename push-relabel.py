from copy import copy, deepcopy

def init(source, residuals, capacities, excesses, heights, n):
  # initialize the heights so that the invariants are met
  for v in range(n):
    heights[v] = 0

  heights[source] = n

  # saturate edges out of the source
  for v in range(n):
    residuals[source][v] = 0
    residuals[v][source] += capacities[source][v]
    excesses[v] += capacities[source][v]

def push(u, v, residuals,  excesses, n):
  delta = min(excesses[u], residuals[u][v])
  residuals[u][v] -= delta
  residuals[v][u] += delta

  excesses[v] += delta
  excesses[u] -= delta

def get_highest(vertices, all_heights):
  current_heights = [all_heights[i] for i in vertices]
  found_vertex = [i for i in vertices if all_heights[i] is max(current_heights)][0]
  return found_vertex

def push_relabel_find_max_flow(s, t, residuals, capacities, excesses, heights, n):
  init(s, residuals, capacities, excesses, heights, n)

  while True:
    nodes_with_left_excess = [v for v in range(n) if excesses[v] > 0 and v not in [s, t]]
    if not nodes_with_left_excess:
      break

    v = get_highest(nodes_with_left_excess, heights)

    downhills = [w for w in range(n) if residuals[v][w] and heights[w] is heights[v] - 1]
    if downhills:
      push(v, downhills[0], residuals, excesses, n)
    else:
      # relabel
      heights[v] += 1

  # result is the flow getting out of the source
  return sum([capacities[0][i] - residuals[0][i] for i in range(n)])

n = 6
capacities = [[0, 16, 13, 0, 0, 0],
              [0, 0, 10, 12, 0, 0],
              [0, 4, 0, 0, 14, 0],
              [0, 0, 9, 0, 0, 20],
              [0, 0, 0, 7, 0, 4],
              [0, 0, 0, 0, 0, 0]]

excesses = [0  for i in range(n)]
heights = [[0] * n for i in range(n)]
residuals = deepcopy(capacities)

f = push_relabel_find_max_flow(0, 5, residuals, capacities, excesses, heights, n)
print f
