# 概要
#
# N個の入力された整数Ai(1 <= i <= 10^9)のすべてが
# 偶数である限り整数を2で割る操作を繰り返し
# その操作を最大で何回行えるかを出力

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