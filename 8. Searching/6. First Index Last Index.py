def find_first(arr, target):
    left, right = -1, len(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid
    return right if right < len(arr) and arr[right] == target else -1


def find_last(arr, target):
    left, right = -1, len(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid
    return left if left >= 0 and arr[left] == target else -1


# Read input
n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Process queries
for _ in range(q):
    x = int(input())
    first = find_first(arr, x)
    last = find_last(arr, x)
    print(f"{first} {last}")
