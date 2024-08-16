# 入力
N, A, B = map(int, input().split())
# 合計
total_sum = 0

for i in range(N + 1):
    # 各桁の数字の和
    digit_sum = sum(map(int, str(i)))
    
    if A <= digit_sum <= B:
        total_sum += i
# 合計を出力
print(total_sum)


