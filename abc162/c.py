import fractions

K = int(input())

gcds = []

for i in range(K):
  g = []
  for j in range(K):
    g.append(fractions.gcd(i + 1, j + 1))
  gcds.append(g)

result = 0

for a in range(K):
  for b in range(K):
    gcd_ab = gcds[a][b]
    for c in range(K):
      result += (gcds[gcd_ab-1][c])

print(result)