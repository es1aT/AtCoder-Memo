"""
二次元配列は一つ目の値を基準に、ソートを行える。
"""
N = int(input())
li = []
for i in range(N):
  S, T = input().split()
  li.append([int(T), S])
li = sorted(li, reverse=True) # li = sorted(li, key=lambda x: x[a]) を用いることでNつ目の値を基準にソート可能。
print(li[1][1])
