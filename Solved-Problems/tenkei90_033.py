H, W = map(int, input().split())
print(H * W if H == 1 or W == 1 else ((H + 1) // 2) * ((W + 1) // 2))
