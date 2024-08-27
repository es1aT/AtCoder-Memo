# 順列で全探索して、XとYが隣り合わない並びから最小値を探す。

import itertools
N = int(input())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
M = int(input())
X, Y = [0]*M, [0]*M
for i in range(M):
  X[i], Y[i] = map(int, input().split())
mi = float("INF")
num = [i for i in range(N)]

for i in itertools.permutations(num):
  flag = True
  for j in range(N-1):
    for k in range(M):
      if (X[k]-1 == i[j] and Y[k]-1 == i[j+1]) or (X[k]-1 == i[j+1] and Y[k]-1 == i[j]):
        flag = False
        break
    if not flag:
      break
  if flag:
    cnt = 0
    for j in range(N):
      cnt += A[i[j]][j]
    mi = min(mi, cnt)

if mi == float("INF"):
  print(-1)
else:
  print(mi)
