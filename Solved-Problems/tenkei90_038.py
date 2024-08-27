# Pythonは多倍長整数が使えるためACとなるが、使えないC++ではWAとなる。
import math
A, B = map(int, input().split())
ans = abs(A * B) // math.gcd(A, B)
print(ans if ans <= 10**18 else "Large")
