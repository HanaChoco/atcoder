# 入力
# お札計N枚, 合計金額Y円
N, Y = map(int, input().split())

#10000円札:x枚, 5000円札:y枚, 1000円札:z枚

# 全探索
for x in range(N + 1):
    for y in range(N - x + 1):
        # 残りの枚数を1000円札
        z = N - x - y
        # 条件を満たすとき,枚数を出力して終了
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()

# 組合せが無かった場合
print(-1, -1 ,-1)

