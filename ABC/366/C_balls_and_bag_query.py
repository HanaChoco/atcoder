# ボールの種類ごとの個数を数える
ball_counts = {}

# 入力
Q = int(input())

for _ in range(Q):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        # ボールを追加
        ball_num = int(query[1])
        ball_counts[ball_num] = ball_counts.get(ball_num, 0) + 1
    elif query_type == 2:
        # ボールを削除
        ball_num = int(query[1])
        if ball_num in ball_counts:
            ball_counts[ball_num] -= 1
            # 個数が0になったボールを辞書から削除
            if ball_counts[ball_num] <= 0:
                del ball_counts[ball_num]
    elif query_type == 3:
        # 出力（種類数のカウント）
        print(len(ball_counts))
