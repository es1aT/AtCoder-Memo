# Nを素因数分解して、何回分割できるか計算する。
def pri_fac(N, li):
    while N % 2 == 0:
        li.append(2)
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            li.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        li.append(N)

N = int(input())
li = []
pri_fac(N, li)

if len(li) == 1:
  print(0)
else:
  cnt, n = 0, len(li)
  while n > 1:
    n = (n + 1) // 2
    cnt += 1
  print(cnt)
