N = int(input())
H = list(map(int, input().split()))

# 攻撃回数の計算
T = 0

for i in range(N):
    if H[i] > 0:
        # 敵1体へのダメージ1の攻撃回数
        T_add = 0
        # 3回攻撃で計5ダメージの付与
        # 体力を3で割ったときの値が攻撃回数でその回数*3のダメージを付与
        T_add = H[i] // 3
        # もとの体力-上記の攻撃回数が通常攻撃の回数でその分のダメージを1付与
        T_add += H[i] - T_add + T_add * 3


    # 攻撃
    # T % 3 == 1:
    #     num = H[i] / 5
    #     T += 3 * num
    #     H[i] -= int(5 * num)
    # else:
    #     T += 1
    #     H[i] -= 1
print(T)
            