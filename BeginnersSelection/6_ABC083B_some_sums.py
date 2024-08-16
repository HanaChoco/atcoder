# 入力
N, A, B = map(int, input().split())

total_sum = 0

for i in range(N + 1):
    # 1以上N以下の整数のうち
    # 10進法での各桁の数字の和が
    # A以上B以下であるものの総和
    if A <= sum(map(int, str(i))) <= B:
        total_sum += i
print(total_sum)


