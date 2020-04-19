import itertools

L, R = map(int, input().split())

R = min(R, L+2019)

minimum = 2018

for c in list(itertools.combinations(list(range(L, R+1)),2)):
    mod = (c[0]*c[1]) % 2019
    if mod < minimum:
        minimum = mod

print(minimum)
