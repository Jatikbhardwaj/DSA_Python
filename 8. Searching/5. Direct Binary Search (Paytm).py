def binary_search(arr, target):
    L = -1
    R = len(arr)

    while L + 1 < R:
        M = (L + R) // 2
        if arr[M] >= target:
            R = M
        else:
            L = M

    return R


# Read input
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Process queries
results = []
for q in queries:
    results.append(binary_search(A, q))

# Output results
print(*results)
