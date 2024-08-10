# 入力
N = int(input())
strings = [input().strip() for _ in range(N)]

# 文字列の長さの最大値
M = max(len(s) for s in strings)

# 縦書き用のリスト
result = [''] * M

# 横書き ⇒ 縦書き
for i in range(M):
    for j in range(N-1, -1, -1):
        if i < len(strings[j]):
            result[i] += strings[j][i]
        else:
            result[i] += '*'

# 各列の末尾が '*' でないように修正
result = [s.rstrip('*') for s in result]

# 出力
for line in result:
    print(line)

