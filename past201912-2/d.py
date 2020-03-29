# https://atcoder.jp/contests/past201912-2/tasks/past201912_d

N = int(input())
A = [int(input()) for i in range(N)]

A = sorted(A)

dup = 0
lack = 0

for i in range(1, N):
    diff = A[i] - A[i-1]
    if diff == 0:
        dup = A[i]
    if diff == 2:
        lack = A[i] - 1

if dup == 0:
    print("Correct")
else:
    if lack == 0:
        lack = N
    print("%s %s" % (dup, lack))
