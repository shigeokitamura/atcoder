# https://atcoder.jp/contests/abc126/tasks/abc126_b

S = input()

YYMM = False
MMYY = False

a, b = int(S[:2]), int(S[2:4])


if a in range(1, 13):
    MMYY = True
if b in range(1, 13):
    YYMM = True


if YYMM and MMYY:
    print("AMBIGUOUS")
elif YYMM and not MMYY:
    print("YYMM")
elif not YYMM and MMYY:
    print("MMYY")
else:
    print("NA")
