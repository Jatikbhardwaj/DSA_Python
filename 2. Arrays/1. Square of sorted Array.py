def square_sorted(arr: list[int]) -> list[int]:
    result = []
    left, right = 0, len(arr)-1

    while left <= right:
        if abs(arr[left]) >= abs(arr[right]):
            result.append(arr[left] * arr[left])
            left += 1
        else:
            result.append(arr[right] * arr[right])
            right -= 1
    return result[::-1]

n = int(input())
arr = list(map(int, input().split()))
resultant_array = square_sorted(arr)
print(*resultant_array)

# TC = O(N)
# SC = O(N)


