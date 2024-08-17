from itertools import product
# 入力
N, K = map(int, input().split())

R = list(map(int, input().split()))

for combination in product(*[range(1, r + 1) for r in R]):
    if sum(combination) % K == 0:
        print(' '.join(map(str, combination)))