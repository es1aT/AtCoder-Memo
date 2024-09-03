"""
flagを用いて、文字列Sが反転を制御。
list()の代わりにdeque()を使用することで、文字列Sの先頭にO(1)で値を追加できる。
"""
from collections import deque
S = deque(input())
Q = int(input())
flag = False
for i in range(Q):
  Query = input().split()
  if len(Query) == 1:
      flag = not flag
  elif len(Query) == 3:
    if Query[1] == "1":
      if flag:
        S.append(Query[2])
      else:
        S.appendleft(Query[2])
    else:
      if flag:
        S.appendleft(Query[2])
      else:
        S.append(Query[2])
if flag:
  S.reverse()
print("".join(S))
