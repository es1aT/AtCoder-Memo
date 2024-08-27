# 制約を利用し、範囲の制限を行う。

N = int(input())
A, B, C = map(int, input().split())
ans = float("INF")

for i in range(min(N//A+1, 9999)):
  for j in range(min((N-i*A)//B+1, 9999)):
    amari = N - i*A - j*B
    if amari % C == 0:
      k = amari // C
      ans = min(ans, i+j+k)
print(ans)
