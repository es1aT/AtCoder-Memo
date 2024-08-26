import math
A, B, C = map(int, input().split())
g = math.gcd(math.gcd(A, B), C)
print(A // g + B // g + C // g - 3)
