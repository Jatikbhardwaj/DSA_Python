n, m = map(int, input().split())
matrix = []
for rows in range(n):
    rows = list(map(int, input().split()))
    matrix.append(rows)

for i in range(n):
    for j in range(i + 1, m):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
matrix = matrix[::-1]

for row in matrix:
    print(*row)
