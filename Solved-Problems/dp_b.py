"""
動的計画法を用いて解く。(PyPyで提出）
（１）地点'i'の最小のコストを格納する'dp'という配列を作り、十分大きな値（無限大など）で初期化する。
（２）すぐに分かるところ(dp[0], dp[1])を埋める。
（３）表の小さいほうから埋めていく。dp[2]では地点'i-1'から'i-K'のそれぞれへジャンプする場合のコストを比較し、最小のものを選ぶ。
（４）答え(dp[N-1])を出力する。
"""

# (1)
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [float("INF")]*N

# (2)
dp[0] = 0
dp[1] = abs(h[0]-h[1])

# (3)
for i in range(2, N):
    for j in range(1, K+1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

# (4)
print(dp[-1])
