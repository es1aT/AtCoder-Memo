# 各行と各列の和を先に計算し、包除原理を用いる。

# 入力値を取得
H, W = map(int, input().split())
A = []
for i in range(H):
  A.append(list(map(int, input().split())))

# 各行と各列の和を格納するリストの初期化
row_sums = [0] * H
col_sums = [0] * W

# 各行と各列の和を計算
for i in range(H):
  for j in range(W):
    row_sums[i] += A[i][j]
    col_sums[j] += A[i][j]

#新しい二次元配列Bに合計した値を格納
B = [[0]*W for _ in range(H)]
for i in range(H):
  for j in range(W):
    B[i][j] = row_sums[i] + col_sums[j] - A[i][j]

# 二次元配列Bを出力
for i in range(H):
  for j in range(W):
    print(B[i][j], end=" ")
  print()
