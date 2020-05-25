from copy import copy, deepcopy

def push(n, u, v, residual,  excesses, h):
  delta = min(excesses[u], residual[u][v])
  residual[u][v] -= delta
  residual[v][u] += delta

  excesses[v] += delta
  excesses[u] -= delta

def init(n, s, r, c, x, h):
  for v in range(n):
    h[v] = 0
  for v in range(n):
    r[s][v] = 0
    r[v][s] += c[s][v]
    x[v] += c[s][v]
  h[s] = n

def find_max_flow(n, r, c, x, h, s, t):
  init(n, s, r, c, x, h)
  while True:
    pos_excesses = sorted([v for v in range(n) if x[v] > 0 and v not in [s, t]])
    if not pos_excesses:
      break
    v = pos_excesses[0]
    downhills = [w for w in range(n) if r[v][w] and h[w] is h[v] - 1]
    if downhills:
      push(n, v, downhills[0], r, x, h)
    else:
      h[v] += 1

  return sum([c[0][i] - r[0][i] for i in range(n) ])

n = 6
c = [[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

f = [[0] * n for i in range(n)]
x = [0  for i in range(n)]
h = [[0] * n for i in range(n)]
r = deepcopy(c)
f = find_max_flow(n, r, c, x, h, 0, 5)
print f
