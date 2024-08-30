N = int(input())
A = list(map(int, input().split()))

# 操作回数のカウンタ
count = 0

while sum(x > 0 for x in A) > 1:
    # 降順に並び替え
    A.sort(reverse=True)
    # A1,A2の要素の値から-1する
    if N > 0:
        A[0] -= 1
    if N > 1:
        A[1] -= 1
    # 操作回数のカウント
    count += 1

print(count)