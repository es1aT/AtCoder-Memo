# ユークリッドの互除法もしくはgcd関数で、三つの値の最大公約数を算出する。
import math
A, B, C = map(int, input().split())
g = math.gcd(math.gcd(A, B), C)
print(A // g + B // g + C // g - 3)
