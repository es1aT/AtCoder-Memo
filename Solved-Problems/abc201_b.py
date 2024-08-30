# 二次元配列は一つ目の値を基準に、ソートを行える。
N = int(input())
li = []
for i in range(N):
  S, T = input().split()
  li.append([int(T), S])
li = sorted(li, reverse=True)
print(li[1][1])
