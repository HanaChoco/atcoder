from itertools import permutations

# 入力の読込
N, K = map(int, input().split())
S = input()
print(N, K, S)

def no_k_palindrome(S, K):
    n = len(S)
    for i in range(n - K + 1):
        substring = S[i:i + K]
        if substring == substring[::-1]:
            return False
    return True

def count_valid_permutations(N, S, K):
    perms = set(permutations(S))
    count = 0
    for perm in perms:
        perm_str = ''.join(perm)
        if no_k_palindrome(perm_str, K):
            count += 1
    return count

result = count_valid_permutations(N, S, K)
print(result)

