# https://atcoder.jp/contests/past201912-2/tasks/past201912_b

N = int(input())

A = [int(input()) for i in range(N)]

for i in range(1, N):
    diff = A[i] - A[i-1]

    if diff == 0:
        print("stay")
    elif diff > 0:
        print("up %s" % diff)
    elif diff < 0:
        print("down %s" % (diff * (-1)))
