# 入力
N = int(input())
# 数字を集合に格納して長さを出力
print(len(set([int(input()) for _ in range(N)])))