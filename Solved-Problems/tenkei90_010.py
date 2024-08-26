N = int(input())
one = [0]*(N+1)
two = [0]*(N+1)

for i in range(1, N+1):
    C, P = map(int, input().split())
    if C == 1:
        one[i] = P
    else:
        two[i] = P

for i in range(1, N+1):
    one[i] += one[i-1]
    two[i] += two[i-1]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(one[R] - one[L-1], two[R] - two[L-1])
