N = int(input()) #典型的な素数の問題
for i in range(2, int(N**0.5)+1):
  if N % i == 0:
    print("NO")
    exit()
print("YES")
