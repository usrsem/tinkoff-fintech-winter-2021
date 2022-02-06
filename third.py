from math import ceil, sqrt

input()

a = list(map(int, input().split()))
xo = 0

for ai in sorted(a, reverse=True):
    xo = sqrt(xo + ai)

print(ceil(xo))
