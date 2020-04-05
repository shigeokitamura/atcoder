# https://atcoder.jp/contests/abc129/tasks/abc129_b

import sys

N = int(input())

W = list(map(int, input().split()))

diff = sys.maxsize

for t in range(N-1):
    s1 = 0
    s2 = 0
    for i in range(t+1):
        s1 += W[i]
    for i in range(t+1, N):
        s2 += W[i]

    if abs(s1-s2) < diff:
        diff = abs(s1-s2)

print(diff)
