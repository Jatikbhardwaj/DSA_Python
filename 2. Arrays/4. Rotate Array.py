n, k = map(int, input().split())
arr = list(map(int, input().split()))


def reverse_array(arr: list, start: int, end: int):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array_inplace(arr: list, rotations: int):
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, rotations - 1)
    reverse_array(arr, rotations, n - 1)
    return arr


print(*rotate_array_inplace(arr, n-k))  # For right rotation, change the order of the reverse_array calls i.e k

# TC = O(N)
# SC = O(1)


# # ** Using Slicing TC O(N) , SC O(N)
# def rotate_left(array, k):
#     return array[k:] + array[:k]
#
#
# def rotate_right(array, k):
#     return array[-k:] + array[:-k]
#
#
# n, k = map(int, input().split())
# array = list(map(int, input().split()))
#
# result = rotate_left(array, k)
# print(*result)
# result = rotate_right(array, k)
# print(*result)
