# https://atcoder.jp/contests/abc129/tasks/abc129_c

N, M = map(int, input().split())

# 壊れている床
a = [-1]
for i in range(M):
  a.append(int(input()))
  # 連続して壊れていたら辿り着けない
  if a[i + 1] - a[i] == 1:
    print(0)
    exit()

# フィボナッチ数列
def fib(n):
  a, b = 0, 1
  if n == 1:
    return a
  elif n == 2:
    return b
  else:
    for i in range(n-2):
      a, b = b, a + b
    return b

# 階段を登る組み合わせ
combi = 1

for i in range(len(a) - 1):
  # 次の穴との距離
  dis = a[i+1] - a[i]
  combi *= fib(dis)

dis = N+1 - a[-1]
combi *= fib(dis)

print(combi % 1000000007)
