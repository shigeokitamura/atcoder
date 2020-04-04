# https://atcoder.jp/contests/abc161/tasks/abc161_b

import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

total_votes = sum(A)
threshold = total_votes * (1 / (4 * M))

chooseable = 0

for a in A:
  if a >= threshold:
    chooseable += 1
    if chooseable >= M:
      print("Yes")
      sys.exit(0)

print("No")