n = 4
a = [[0, 2, 1, 2], [2, 0, 2, 1], [1, 2, 0, 2], [2, 1, 2, 0]]

def permutation(lst):
  n = len(lst)
  if not n:
    return []
  if n == 1:
    return [lst]

  res = []
  for i in range(n):
    m = lst[i]
    rm_lst = lst[:i] + lst[i+1:]
    for p in permutation(rm_lst):
      res.append([m] + p)
  return res

# calculate turning points in a list of 1-4 with |i-j| = 2
def is_alternating(a):
  f_ip = a[0] < a[1] and a[1] > a[2] or a[0] > a[1] and a[1] < a[2]
  s_ip = a[2] < a[3] and a[3] > a[4] or a[2] > a[3] and a[3] < a[4]
  return f_ip and s_ip

# print permutation(range(6))
print len([p for p in permutation(range(1, 6)) if is_alternating(p)])

def try_path(path):
  d = 0
  for i in range(3):
    if a[path[i]][path[i+1]] == 0:
      return float("Inf")
    d += a[path[i]][path[i+1]]
  return d

def find_paths():
  m = float("Inf")
  res = None
  for p in permutation(range(4)):
    d = try_path(p)
    if d <= m:
      m = d
      res = p
  return res, m

# print find_paths()