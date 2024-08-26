N, K = map(int, input().split()) # 典型的な二分探索問題
A = list(map(int, input().split()))
left, right = 0, N-1
while left <= right:
  mid = (left + right) // 2
  if A[mid] >= K:
    right = mid - 1
  else:
    left = mid + 1
  
if left == N:
  print(-1)
else:
  print(left)
