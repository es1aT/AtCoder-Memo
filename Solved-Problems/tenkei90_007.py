#二分探索して、生徒のレーティングに最も近いクラスを探す。

N = int(input()) # クラス数
A = sorted(list(map(int, input().split()))) # クラスの推奨レーティング
Q = int(input()) # 生徒数
for i in range(Q): # 生徒のレーティング
  B = int(input())
  left, right = 0, N-1
  while left <= right:
    mid = (left + right) // 2
    if A[mid] >= B:
      right = mid - 1
    else:
      left = mid + 1
  if left == N:
      print(abs(A[left-1] - B))
  elif left == 0:
      print(abs(A[0] - B))
  else:
      print(min(abs(A[left] - B), abs(A[left-1] - B)))
