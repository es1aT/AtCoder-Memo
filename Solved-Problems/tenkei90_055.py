N, P, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
cnt = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      for l in range(k+1, N):
        for n in range(l+1, N):
          if A[i]*A[j]%P*A[k]%P*A[l]%P*A[n]%P == Q:
            cnt += 1
print(cnt)
