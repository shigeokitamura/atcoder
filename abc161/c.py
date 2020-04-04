# https://atcoder.jp/contests/abc161/tasks/abc161_c

N, K = map(int, input().split())

x = N - (N // K) * K
ans1 = abs(x - K)
ans2 = abs(ans1 - K)
print(min(ans1, ans2))
