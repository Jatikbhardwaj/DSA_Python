def union_of_arrays(arr1, arr2):
    union_set = set()
    for num in arr1:
        union_set.add(num)
    for num in arr2:
        union_set.add(num)
    return union_set


n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
result = union_of_arrays(N, M)
sorted_result = sorted(result)
print(*sorted_result)


# Time Complexity: O((N+M)log(N+M))
# Space Complexity: O(N+M)