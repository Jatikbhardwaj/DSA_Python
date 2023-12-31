# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     rows = list(map(int, input().split()))
#     matrix.append(rows)
# transpose = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         transpose[j][i] = matrix[i][j]

# for row in transpose:
#     print(*row)

# TC = O(n*m)
# SC = O(n*m)

# Using Inplace Transpose 
n, m = map(int,input().split())
matrix = []
for rows in range(n):
    rows = list(map(int,input().split()))
    matrix.append(rows)

for i in range(n):
    for j in range(i + 1, m):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for rows in matrix:
    print(*rows)

# TC = O(n*m)
# SC = O(1)