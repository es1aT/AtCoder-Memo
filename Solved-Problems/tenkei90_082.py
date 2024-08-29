# 等差数列の公式を用いて、計算量を減らす。
# ｛（最初の数＋最後の数）×（最後の数－最初の数+1）/ 2｝× 桁数 

L, R = map(int, input().split())
A = []
for i in range(1, 1000):
    A.append((10**(i-1) + 10**i-1) * (10**i-1 -10**(i-1) + 1) // 2 * i)

cnt = 0
len_L = len(str(L))
len_R = len(str(R))
if len_L == len_R: # 桁数が同じときは等差数列の和の公式を使い、桁数を掛ける。
  cnt = (R + L) * (R -L + 1) // 2 * len_L
else: # 桁数が違う場合は、「Lの桁＋中間の桁＋Rの桁」を計算する。
  cnt += (L + 10**len_L-1) * (10**len_L -(L+1) + 1) // 2 * len_L # Lの桁の総和
  for i in range(len_L+1, len_R): # 中間の桁の総和
      cnt += A[i-1]
  cnt += (10**(len_R-1) + R) * (R -10**(len_R-1) + 1) // 2 * len_R # Rの桁の総和
print(cnt % (10**9 + 7))
