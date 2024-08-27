# A < Bであるため、abs(A - B)とBから大きい順に取得するだけでよい。
N, K = map(int, input().split())
li = []
for i in range(N):
  A, B = map(int, input().split())
  li.append(abs(A - B))
  li.append(B)
print(sum(sorted(li, reverse=True)[:K]))
