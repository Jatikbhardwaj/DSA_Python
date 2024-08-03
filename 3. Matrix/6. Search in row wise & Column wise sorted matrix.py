n, m = map(int, input().split())
matrix = []
for i in range(n):
    rows = list(map(int, input().split()))
    matrix.append(rows)
x = int(input())

i, j = 0, m - 1
while i < n and j >= 0:
    if matrix[i][j] == x:
        print(f"Found at matrix[{i}][{j}]")
    if matrix[i][j] > x:
        j -= 1
    else:
        i += 1

# TC = O(n + m)
# SC = O(1)
