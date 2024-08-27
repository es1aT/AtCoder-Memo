# 二進数にして全探索する
N = int(input())
for i in range(2**N):
  mo = format(i, "0" + str(N) + 'b').replace('1', ')').replace('0', '(')
  kakko = 0
  flag = True
  for i in mo:
    if i == "(":
      kakko += 1
    else:
      kakko -= 1
    if kakko < 0 or (i != "(" and i != ")"):
      flag = False
      break
  if flag and kakko == 0:
    print(mo)
