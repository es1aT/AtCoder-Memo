N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += abs(A[i] - B[i])
print("Yes" if K >= cnt and (K - cnt) % 2 == 0 else "No")
