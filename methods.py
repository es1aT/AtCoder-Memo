def convert(num, n, m): # n進数をm進数に変換する（全て数字で入力）
    decimal = int(str(num), n) # 10進数に変換
    if decimal == 0:
        return "0" # 元が0なら"0"を返す
    else:
        digits = []
        while decimal > 0:
            digits.append(str(decimal % m))
            decimal //= m
        return "".join(reversed(digits)) # 結果を文字列で返す
