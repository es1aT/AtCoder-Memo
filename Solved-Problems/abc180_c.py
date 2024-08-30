# 以下のような約数列挙を行うと、O(√N)で解ける。
N = int(input())
li = []
for i in range(1, int(N**0.5)+1): 
  if N % i == 0:
    print(i) 
    if i != N // i:
      li.append(N // i) #print(i)したものとペアとなる約数を配列に追加
for i in range(len(li)-1, -1, -1):
  print(li[i])
