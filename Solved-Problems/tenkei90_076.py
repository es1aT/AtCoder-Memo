# 円環を倍にして結合し、しゃくとり法で全体の大きさの10分の1になるものを探す。
N = int(input())
A = list(map(int, input().split()))
yaa = sum(A) / 10
if yaa % 1 != 0:
  print("No")
  exit()
A += A

head, tail, cnt = 0, 0, 0
while head < N*2 and tail < N*2:
  if cnt > yaa:
    cnt -= A[tail]
    tail += 1
  elif cnt < yaa:
    cnt += A[head]
    head += 1
  else:
    print("Yes")
    exit()
print("No")
