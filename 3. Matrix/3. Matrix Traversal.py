n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
output = []
top, bottom, left, right = 0, n - 1, 0, m - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        output.append(matrix[top][j])
    top += 1
    for i in range(top, bottom + 1):
        output.append(matrix[i][right])
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            output.append(matrix[bottom][j])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            output.append(matrix[i][left])
        left += 1
print(*output)
