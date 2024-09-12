"""
都市と道路の関係を表す隣接リストを作成し、
それぞれの都市から他の都市への組を幅優先探索でカウントする。
"""
from collections import deque

N, M = map(int, input().split())
connect = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)

cnt = N # スタートとゴールの都市が同じという組み合わせがN通りある
for i in range(1, N+1):
  queue = deque([i])
  visited = [False]*(N+1)
  visited[i] = True
  while queue:
    node = queue.popleft()
    for nbr in connect[node]:
      if visited[nbr] == False:
        visited[nbr] = True
        queue.append(nbr)
        cnt += 1
print(cnt)
