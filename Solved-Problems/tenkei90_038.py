# Pythonは多倍長整数が使えるためACとなるが、使えないC++ではWAとなり対策が必要である。
import math
A, B = map(int, input().split())
ans = abs(A * B) // math.gcd(A, B)
print(ans if ans <= 10**18 else "Large")
