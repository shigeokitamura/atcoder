# https://atcoder.jp/contests/past201912-2/tasks/past201912_d

S = input()

if (S.isdigit() and len(S) == 3):
    print(int(S) * 2)
else:
    print("error")
