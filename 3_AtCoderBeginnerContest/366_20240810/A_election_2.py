# 入力
n, t, a = map(int, input().split())

# 投票の合計
total_votes = t + a

# 残りの投票数
remaining_votes = n - total_votes

# 高橋氏が勝つ条件
if t > a + remaining_votes:
    print("Yes")
# 青木氏が勝つ条件
elif a > t + remaining_votes:
    print("Yes")
# どちらの勝利も確定しない場合
else:
    print("No")
