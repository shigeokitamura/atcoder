# https://atcoder.jp/contests/abc126/tasks/abc126_a

N, K = map(int, input().split())
S = input()
S_ = ""
for i in range(N):
    if i == K-1:
        S_ += S[i].lower()
    else:
        S_ += S[i]

print(S_)