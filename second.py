n, m = map(int, input().split())
counter = 0

while n and m != 0:
    if (n > m):
        n, m = n - m, m
    else:
        n, m = m - n, n

    counter += 1

print(counter)

