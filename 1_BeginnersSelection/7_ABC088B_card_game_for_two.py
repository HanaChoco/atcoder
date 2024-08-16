# 入力
N = int(input())
a = list(map(int, input().split()))

# カードを降順に並べ替え
a.sort(reverse=True)

# 点数が高い順から1枚ずつ交互に取る
# 偶数番目をアリス、貴数番目をボブが取る
alice_score = sum(a[::2])
bob_score = sum(a[1::2])

# 差を出力
print(alice_score - bob_score)