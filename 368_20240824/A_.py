N, K = map(int, input().split())
A = list(map(int, input().split()))

print(" ".join(map(str, A[N-K:] + A[:N-K])))