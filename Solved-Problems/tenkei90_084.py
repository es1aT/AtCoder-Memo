# ランレングス圧縮を行うことで、O(N)で解ける。
def сжатие():
  li = []
  cnt = 1
  for i in range(1, N):
    if S[i] == S[i-1]:
      cnt += 1
    else:
      li.append(cnt)
      cnt = 1
  li.append(cnt)
  return li

N = int(input())
S = list(input())
li = сжатие()

su, ans = sum(li), 0
for i in li:
  su -= i
  ans += su * i
print(ans)


# しゃくとり法でも解けた。
N = int(input())
S = list(input())
tail = ans = 0
for head in range(N):
  symbol = S[head]
  while tail < N and symbol == S[tail]:
    tail += 1
  ans += N - tail
print(ans)
