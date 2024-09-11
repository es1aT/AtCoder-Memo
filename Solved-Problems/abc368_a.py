"""
（１）スライスの基本構文を使って処理を行う。
（２）collectionモジュールのdeque型にあるローテート機能を用いる。
"""
# (1)
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = A[-K:] + A[:-K]
for i in A:
  print(i, end=" ")

# (2)
from collections import deque
N, K = map(int, input().split())
A = deque(map(int, input().split()))
A.rotate(K)
for i in A:
  print(i, end=" ")
