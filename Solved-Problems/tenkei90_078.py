# 隣接リストを用いる
N, M = map(int, input().split())
li = [[] for _ in range(N)]
ans = 0

for i in range(M):
  a, b = map(int, input().split())
  li[a-1].append(b)
  li[b-1].append(a)

for i in range(N):
  cnt = 0
  for j in range(len(li[i])):
    if li[i][j] < i+1:
      cnt += 1
  if cnt == 1:
    ans += 1

print(ans)
