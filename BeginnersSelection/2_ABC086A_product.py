# 正の整数a, bの積の偶数・奇数判定

# 入力
a, b = map(int, input().split())


if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
