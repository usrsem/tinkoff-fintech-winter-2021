n, m = map(int, input().split())

F = [[0] * (m+1) for _ in range(n+1)]
F[1][1] = 1

for i in range(2, n+1):
    for j in range(2, m+1):
        F[i][j] = F[i-1][j-2] + F[i-2][j-1]

print(F[n][m])
