# 入力の読込
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

# print(N, T, P, L)

# 初期条件の確認
count = sum(1 for length in L if length >= T)
if count >= P:
    print(0)
else:
    #日数の計算
    days = 0
    while count < P:
        days += 1
        count = sum(1 for length in L if(length + days >= T)) 
    print(days)


