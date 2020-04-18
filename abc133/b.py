import math
import itertools

N, D = map(int, input().split())

X = [[0]*(D+1)]*(N+1)

for n in range(N):
    X[n] = list(map(int, input().split()))

def distance(x, y):
    dis = 0
    for d in range(D):
        dis += abs(x[d] - y[d]) ** 2

    return math.sqrt(dis).is_integer()

distance(X[1], X[2])

count = 0

for c in itertools.combinations(list(range(N)), 2):
    if distance(X[c[0]], X[c[1]]):
        count += 1

print(count)
