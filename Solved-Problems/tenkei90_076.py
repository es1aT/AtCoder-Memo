# 円環を倍にして結合し、しゃくとり法で全体の大きさの10分の1になるものを探す。
N = int(input())
A = list(map(int, input().split()))
want = sum(A) / 10
if want % 1 != 0:
  print("No")
  exit()
A += A

tail, cnt = 0, 0
for head in range(N*2):
  cnt += A[head]
  while cnt > want:
    cnt -= A[tail]
    tail += 1
  if cnt == want:
    print("Yes")
    exit()
print("No")
