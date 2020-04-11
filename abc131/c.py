import math
import fractions

A, B, C, D = map(int, input().split())

def lcm(a, b):
  return (a * b) // fractions.gcd(a, b)

# Cで割り切れる数
divC = B // C - (A-1) // C

# Dで割り切れる数
divD = B // D - (A-1) // D

# CとDの最小公倍数で割り切れる数
lcmCD = lcm(C, D)
divCD = B // lcmCD - (A-1) // lcmCD

# CとDの少なくとも一方で割り切れる数
divCorD = divC + divD - divCD

# AからBまでの数
AB = B - A + 1

print(AB - divCorD)