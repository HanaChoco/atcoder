# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 各休憩所における累積歩数を格納するリスト
sum_steps = [0] * (N + 1)

# 累積歩数の計算
for i in range(1, N + 1):
    sum_steps[i] = sum_steps[i - 1] + A[i - 1]

# 適する(s, t)の組み合わせの数
count = 0

# 開始位置が終了位置よりも前の場合の計算
for start in range(1, N + 1):
    for end in range(start + 1, start + N + 1):
        # 終了位置を1～Nに収める
        end_mod = end % N
        if end_mod == 0:
            end_mod = N

        # 歩数の合計を計算
        if end_mod > start:
            total_steps = sum_steps[end_mod] - sum_steps[start - 1]
        else:
            total_steps = sum_steps[N] - sum_steps[start - 1] + sum_steps[end_mod]
        
        # 歩数の合計がMの倍数であるか確認
        if total_steps % M == 0:
            count += 1

# 結果を出力
print(count)
