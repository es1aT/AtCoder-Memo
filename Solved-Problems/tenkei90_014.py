# それぞれソートして、貪欲法を用いる。

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
cnt = 0
for i in range(N):
  cnt += abs(A[i] - B[i])
print(cnt)
