N, K = map(int, input().split()) # スライスを用いる問題
A = list(map(int, input().split()))
A = A[-K:] + A[:-K]
for i in A:
  print(i, end=" ")
