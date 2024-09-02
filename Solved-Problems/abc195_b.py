# みかん一個の重さは整数とは限らず全探索できないため、みかんの個数で全探索を行う。
A, B, W = map(int, input().split())
mi = 10**15
ma = -10**15
for i in range(1, 10**6+10):
  if A * i <= W * 1000 <= B * i:
    mi = min(mi, i)
    ma = max(ma, i)

if mi==10**15:
  print("UNSATISFIABLE")
else:
  print(mi, ma)
