

# しゃくとり法でも解ける。
N = int(input())
S = list(input())
tail = ans = 0
for head in range(N):
  symbol = S[head]
  while tail < N and symbol == S[tail]:
    tail += 1
  ans += N - tail
print(ans)
