N, K = map(int, input().split())
A = list(map(int, input().split()))
A = A[-K:] + A[:-K]
for i in A:
  print(i, end=" ")
