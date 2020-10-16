arrito = [0, 3, 3, 7, 5, 3, 11, 1]
def solution(A):
  arr2 = sorted(A)
  n = len(A)
  indices_in_sorted = {}
  for i in range(n):
    indices_in_sorted[str(arr2[i])] = i

  minimum = float("Inf")
  for i in range(n):
    for j in range(n):
      i_in_sorted = indices_in_sorted[str(A[i])]
      if i_in_sorted == n-1:
        break
      if arr2[i_in_sorted + 1] == A[j]:
        if abs(i - j) <= minimum:
          minimum = abs(i-j)
  return minimum

print(solution(arrito))
