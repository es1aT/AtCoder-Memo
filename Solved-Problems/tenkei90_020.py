# 浮動小数点の誤差を考慮する必要がある。

# 問題の通りの解法（誤差のためにWAとなる）
import math
a, b, c = map(int, input().split())
print("Yes" if math.log(a, 2) < math.log(c**b, 2) else "No")

# 数式を単純化した解法（ACとなる）
import math
a, b, c = map(int, input().split())
print("Yes" if a < c**b else "No")
