# def binary_search_first_one(n, arr):
#     L = 0
#     R = n - 1
#     while L + 1 < R:
#         M = (L + R) // 2
#         if arr[M] == 0:
#             L = M
#         else:
#             R = M
#
#     if R < n:
#         return R
#     else:
#         return -1
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# result = binary_search_first_one(n, arr)
# print(result)

def binary_search_last_zero(n, arr):
    L = 0
    R = n - 1
    while L + 1 < R:
        M = (L + R) // 2
        if arr[M] == 0:
            L = M
        else:
            R = M

    if L >= 0:
        return L
    else:
        return -1


n = int(input())
arr = list(map(int, input().split()))
result = binary_search_last_zero(n, arr)
print(result)
