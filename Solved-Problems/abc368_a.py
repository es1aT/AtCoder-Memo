# スライスの基本構文を使って処理を行う。

# 入力値を取得
N, K = map(int, input().split())
A = list(map(int, input().split()))

# リストAをK回右に回転させる
A = A[-K:] + A[:-K]

# 結果を出力
for i in A:
  print(i, end=" ")
