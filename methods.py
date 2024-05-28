def convert(num, n, m): # n進数をm進数に変換する（全て数字で入力、2~10まで）
    decimal = int(str(num), n) # 10進数に変換
    if decimal == 0:
        return 0 # 元が0なら0を返す
    else:
        digits = []
        while decimal > 0:
            digits.append(str(decimal % m))
            decimal //= m
        return int("".join(reversed(digits))) # 結果を数字で返す
