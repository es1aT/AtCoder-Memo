"""
O(N^2)の場合、CPythonで実行すると1658msでTLEとなるが、PyPyなら157msでACとなる。
PyPyなら動くかどうかの見極めが必要。
"""
N = int(input())
A = list(map(int, input().split()))
tail, ma = 0, 0
for head in range(N):
  mi = A[head]
  tail = head
  while tail < N:
    mi = min(mi, A[tail])
    ma = max(ma, mi * (tail - head + 1))
    tail += 1
print(ma)
