def convert(num, n, m):  # n進数をm進数に変換
    decimal = int(str(num), n)  # 10進数に変換
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        result = str(decimal % m) + result
        decimal //= m
    return result
