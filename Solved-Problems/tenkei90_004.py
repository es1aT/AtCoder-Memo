H, W = map(int, input().split())
A = []
B = [[0]*W for _ in range(H)]
I = [0]*H
J = [0]*W
for i in range(H):
  A.append(list(map(int, input().split())))

for i in range(H):
  for j in range(W):
    I[i] += A[i][j]
for j in range(W):
  for i in range(H):
    J[j] += A[i][j]

cnt = 0
for i in range(H):
  for j in range(W):
    B[i][j] = I[i] + J[j] - A[i][j]
for i in range(H):
  for j in range(W):
    print(B[i][j], end=" ")
  print()
