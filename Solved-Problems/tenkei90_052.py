N = int(input())
A = []
cnt = 1
for i in range(N):
  cnt *= sum(list(map(int, input().split())))
print(cnt % (10**9 + 7))
