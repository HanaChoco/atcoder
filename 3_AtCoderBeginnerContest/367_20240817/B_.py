X = float(input())

# 小数点以下が0なら整数で出力
if X.is_integer():
    print(int(X))
else:
    print(X)