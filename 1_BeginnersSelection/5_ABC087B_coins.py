# 入力

# a, b, c, d = [int(input()) for _ in range(4)]

a = int(input()) # 500円玉
b = int(input()) # 100円玉
c = int(input()) # 50円玉
x = int(input()) # 合計金額

count = 0

# 全探索
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            # 合計金額がX円になる場合、カウントする
            if 500 * i + 100 * j + 50 * k == x:
                count += 1

print(count)