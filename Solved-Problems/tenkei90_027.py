# set型を用いる解法
N = int(input())
a = set()
for i in range(N):
  S = input()
  if S not in a:
    a.add(S)
    print(i+1)


# 辞書を用いる解放
N = int(input())
a = {}
for i in range(N):
  S = input()
  if S not in a:
    a[S] = True
    print(i+1)
