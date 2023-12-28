n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


def snake_matrix(matrix):
    for row in range(n):
        if row % 2 == 0:
            print(*matrix[row], end=" ")
        else:
            print(*matrix[row][::-1], end=" ")


result = snake_matrix(matrix)
