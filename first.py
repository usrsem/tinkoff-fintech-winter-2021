a, b, n = map(int, input().split())
diff = a - b

if diff % 2 == 0 and diff >= 2 * n:
    print('YES')
else:
    print('NO')
