# A matrix  is said to be toeplitz if every diagonal (of all sizes) from the top-left to the bottom-right has the same elements.
n, m = map(int, input().split())
matrix = []
for rows in range(n):
    rows = list(map(int, input().split()))
    matrix.append(rows)

for i in range(n - 1):
    for j in range(m - 1):
        if matrix[i][j] != matrix[i + 1][j + 1]:
            print(0)
            exit(0)
print(1)

# TC = O(n*m)
# SC = o(n*m)
