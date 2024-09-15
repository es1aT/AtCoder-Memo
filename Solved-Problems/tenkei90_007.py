"""
生徒のレーティングに最も近いクラスを探す方法には以下の二種類がある。
(1) 二分探索のアルゴリズムを作成する。
(2) bisectモジュールを用いる。
"""

# (1)
# 入力値を取得
N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

# 各生徒のレーティングに対して最も近いクラスを探す。
for i in range(Q):
  B = int(input())
  left, right = 0, N-1
  while left <= right: # 二分探索
    mid = (left + right) // 2
    if A[mid] >= B:
      right = mid - 1
    else:
      left = mid + 1

  # 最も近いクラスのレーティングを出力
  if left == N:
      print(abs(A[left-1] - B))
  elif left == 0:
      print(abs(A[0] - B))
  else:
      print(min(abs(A[left] - B), abs(A[left-1] - B)))

# (2)
import bisect

# 入力値を取得
N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

# 各生徒のレーティングに対して最も近いクラスを探す
for i in range(Q):
    B = int(input())
    pos = bisect.bisect_left(A, B)
    
    # 最も近いクラスのレーティングを出力
    if pos == N:
        print(abs(A[N-1] - B))
    elif pos == 0:
        print(abs(A[0] - B))
    else:
        print(min(abs(A[pos] - B), abs(A[pos-1] - B)))
