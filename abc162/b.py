N = int(input())

result = 0

for i in range(N):
  if (i + 1) % 5 == 0:
    continue
  elif (i + 1) % 3 == 0:
    continue
  else:
    result += (i + 1)

print(result)