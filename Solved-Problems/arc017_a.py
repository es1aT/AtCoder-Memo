# 典型的な素数の問題

# 入力値を取得
N = int(input())

# 素数判定
for i in range(2, int(N**0.5)+1):
  if N % i == 0:
    print("NO") # Nが素数でない場合
    exit()
print("YES") # Nが素数である場合
