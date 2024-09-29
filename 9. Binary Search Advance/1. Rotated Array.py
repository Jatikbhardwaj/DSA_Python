def find_minimum(arr):
    left, right = 0, len(arr) - 1

    # If the array is not rotated at all
    if arr[left] <= arr[right]:
        return arr[left]

    while left < right:
        mid = left + (right - left) // 2

        # If mid is greater than its next element, then mid+1 is the minimum
        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]

        # If mid is less than its previous element, then mid is the minimum
        if arr[mid] < arr[mid - 1]:
            return arr[mid]

        # If the left part is sorted, then the minimum is in the right part
        if arr[left] <= arr[mid]:
            left = mid + 1
        # Otherwise, the minimum is in the left part
        else:
            right = mid - 1

    # If we reach here, left == right, and this is the minimum element
    return arr[left]


# Fast input
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# Find and print the minimum
print(find_minimum(arr))
