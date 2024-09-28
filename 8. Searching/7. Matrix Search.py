def binary_search(matrix, target, n, m):
    print(matrix)
    left, right = 0, n * m - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // m, mid % m
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, -1

import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queries = list(map(int, input().split()))

for query in queries:
    row, col = binary_search(matrix, query, n, m)
    print(row, col)

# Time Complexity:
#
# For each query, we perform a binary search on N*M elements.
# Therefore, the time complexity is O(Q * log(N*M)), where Q is the number of queries.
# Space Complexity:
#
# O(N*M) to store the matrix.
# O(Q) to store the queries.