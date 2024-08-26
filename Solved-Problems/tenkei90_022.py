# ユークリッドの互除法もしくはgcd関数で、三つの値の最大公約数を算出する。

# mathのgcd関数を用いた場合
import math
A, B, C = map(int, input().split())
g = math.gcd(math.gcd(A, B), C)
print(A // g + B // g + C // g - 3)


#ユークリッドの互除法を用いた場合
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
A, B, C = map(int, input().split())
g = gcd(gcd(A, B), C)
print(A // g + B // g + C // g - 3)
