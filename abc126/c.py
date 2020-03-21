# https://atcoder.jp/contests/abc126/tasks/abc126_c

import math

N, K = map(int, input().split())

a = 0

for i in range(1, N+1):
    x = 0
    while(i * pow(2, x) < K):
        x += 1

    a += 1/N * pow(1/2, x)

print(a)
