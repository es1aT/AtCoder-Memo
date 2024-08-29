# 先に全ての値の46の余りを算出し、数字ごとにグループ分けを行う。

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
Acnt = [0] * 46
Bcnt = [0] * 46
Ccnt = [0] * 46
for i in range(N):
    Acnt[A[i] % 46] += 1
    Bcnt[B[i] % 46] += 1
    Ccnt[C[i] % 46] += 1
cnt = 0
for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i + j + k) % 46 == 0:
        cnt += Acnt[i] * Bcnt[j] * Ccnt[k]
print(cnt)
