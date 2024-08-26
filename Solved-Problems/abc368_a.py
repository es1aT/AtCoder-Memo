N, K = map(int, input().split()) # スライスの基本構文を用いる。
A = list(map(int, input().split()))
A = A[-K:] + A[:-K]
for i in A:
  print(i, end=" ")
