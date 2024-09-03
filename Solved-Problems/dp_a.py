"""
動的計画法を用いて解く。
（１）地点'i'の最小のコストを格納する'dp'という配列を作る。
（２）すぐに分かるところ(dp[0], dp[1])を埋める。
（３）表の小さいほうから埋めていく。dp[2]では地点'i-1'と'i-2'からジャンプする場合のコストを比較する。
（４）答え(dp[N-1])を出力する。
"""

N = int(input())
h = list(map(int, input().split()))
dp = [0]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])
for i in range(2, N):
  dp[i] = min(dp[i-2] + abs(h[i-2]-h[i]), dp[i-1] + abs(h[i-1]-h[i]))
print(dp[-1])
