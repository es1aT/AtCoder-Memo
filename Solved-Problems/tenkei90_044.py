# 配列のインデックスがマイナスになると、配列の最後尾が指定される仕様を利用する。

# 普通に解いた場合（TLEとなる）
N, Q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(Q):
  T, x, y = map(int, input().split())
  if T == 1:
    A[x-1], A[y-1] = A[y-1], A[x-1]
  if T == 2:
    A.insert(0, A[-1])
    A.pop(-1)
  if T == 3:
    print(A[x-1])

# 見かけ上のシフトを行い高速化した場合（ACとなる）
N, Q = map(int, input().split())
A = list(map(int, input().split()))
start = 0
for i in range(Q):
  T, x, y = map(int, input().split())
  if T == 1:
    A[(start+x-1)%N], A[(start+y-1)%N] = A[(start+y-1)%N], A[(start+x-1)%N]
  if T == 2:
    start = (start-1) % N
  if T == 3:
    print(A[(start+x-1)%N])
