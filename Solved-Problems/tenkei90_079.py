# 操作の順序は気にせずにi=j=0から調整していき、i=H-1とj=W-1の列の数字が等しいかを判定する。
H, W = map(int, input().split())
A = []
B = []
for i in range(H):
  A.append(list(map(int, input().split())))
for i in range(H):
  B.append(list(map(int, input().split())))
cnt = 0
for i in range(H-1):
  for j in range(W-1):
    sa = B[i][j] - A[i][j]
    if sa != 0:
      A[i][j] += sa
      A[i+1][j] += sa
      A[i][j+1] += sa
      A[i+1][j+1] += sa
      cnt += abs(sa)

flag = True
for i in range(H):
  for j in range(W):
    if A[i][j] != B[i][j]:
      flag = False
if flag:
  print("Yes")
  print(cnt)
else:
  print("No")
