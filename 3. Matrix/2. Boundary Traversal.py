n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
output = []
if n > 1 and m > 1:
    for j in range(m):
        output.append(matrix[0][j])  # Top row

    for i in range(1, n - 1):
        output.append(matrix[i][m - 1])  # Right column

    for j in range(m - 1, -1, -1):
        output.append(matrix[n - 1][j])  # Bottom row

    for i in range(n - 2, 0, -1):
        output.append(matrix[i][0])  # Left column
print(*output)

# for i in range(n):
#     for j in range(m):
#         if i == 0 or j == 0 or i == n - 1 or j == m - 1:
#             print(matrix[i][j], end=" ")
# TC = O(N * M)
