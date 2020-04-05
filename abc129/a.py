# https://atcoder.jp/contests/abc129/tasks/abc129_a

P, Q, R = map(int, input().split())

min = P + Q

if R + Q < min:
    min = R + Q

if P + R < min:
    min = P + R

if Q + R < min:
    min = Q + R

if R + P < min:
    min = R + P

if Q + P < min:
    min = Q + P

print(min)
