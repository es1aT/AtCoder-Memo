"""
制約が1<=N,M<=12と非常に小さいため、bit全探索を行うことで解ける。
"""
N, M, X = map(int, input().split())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
mi = float("INF")
for i in range(2**N):
  order = list(format(i, "0" + str(N) + 'b'))
  total = 0
  li = [0]*M
  for j in range(len(order)):
    if order[j] == "1":
      total += A[j][0]
      for k in range(M):
        li[k] += A[j][k+1]
  flag = True
  for j in range(M):
    if li[j] < X:
      flag = False
  if flag:
    mi = min(mi, total)
print(mi if mi != float("INF") else -1)
