def max_candy_types(n):
    left, right = 0, 10**18  # Set a large upper bound
    while left <= right:
        mid = (left + right) // 2
        cost = (mid * (mid + 1)) // 2
        if cost <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right

import sys

input = sys.stdin.readline
n = int(input())
result = max_candy_types(n)
print(result)
