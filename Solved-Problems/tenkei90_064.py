# 隣り合う二つの要素の差を変化させて、出力する。
N, Q = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
diff = [0]*N
for i in range(N-1):
  diff[i] = A[i+1] - A[i]
for i in range(len(diff)):
  cnt += abs(diff[i])
ans = cnt

for i in range(Q):
  L, R, V = map(int, input().split())
  bef = abs(diff[L-2]) + abs(diff[R-1])
  if L-1 != 0:
    diff[L-2] += V
  if R-1 != N-1:
    diff[R-1] -= V
  aft = abs(diff[L-2]) + abs(diff[R-1])
  ans += aft - bef
  print(ans)
