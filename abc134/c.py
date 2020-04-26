N = int(input())
A = [int(input()) for i in range(N)]

A_max = max(A)
A_second = A_max

if A.count(A_max) == 1:
  AA = []
  for a in A:
    if a != A_max:
      AA.append(a)
  A_second = max(AA)

for i in range(len(A)):
  if A[i] == A_max:
    print(A_second)
  else:
    print(A_max)