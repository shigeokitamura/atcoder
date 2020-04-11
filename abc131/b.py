import copy

N, L = map(int, input().split())

taste = []
for i in range(1, N+1):
    taste.append(L+i-1)

plan = sum(taste)

diff = []
ans = []

for i in range(0, N):
    apples = copy.deepcopy(taste)
    apples.pop(i)
    diff.append(abs(plan - sum(apples)))
    ans.append(sum(apples))

print(ans[diff.index(min(diff))])