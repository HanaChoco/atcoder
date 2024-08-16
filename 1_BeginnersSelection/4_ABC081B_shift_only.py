# 入力
N = int(input())
A = list(map(int, input().split()))

count = 0

# Aに格納された数字全てが偶数のとき
while all(a % 2 == 0 for a in A):
    # 整数全てを2で割ったものに置き換え
    A = [a // 2 for a in A]
    # 上記の操作回数
    count += 1

print(count)