# 因数分解を行って、先に足し算する。
N = int(input())
cnt = 1
for i in range(N):
  cnt *= sum(list(map(int, input().split())))
print(cnt % (10**9 + 7))
