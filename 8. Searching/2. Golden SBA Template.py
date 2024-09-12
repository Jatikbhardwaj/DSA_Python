# def golden_template_binary_search_first(arr, X):
#     def predicate(M):
#         if arr[M] < X:
#             return 0
#         else:
#             return 1
#
#     L = -1
#     R = len(arr)
#
#     while L + 1 < R:
#         M = (L + R) // 2
#         if predicate(M) == 0:
#             L = M
#         else:
#             R = M
#
#     # Handle edge cases and return result
#     if R < len(arr) and arr[R] == X:
#         return R
#     else:
#         return -1  # X not found in the array
#
# # Test the function
# arr = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
# X = 5
# result = golden_template_binary_search_first(arr, X)
# print(f"First occurrence of {X} is at index: {result}")
#
# # Edge case: X not in array
# X = 9
# result = golden_template_binary_search_first(arr, X)
# print(f"First occurrence of {X} is at index: {result}")

# The Golden Template Rule steps:
#
# Verify monotonicity: Is the problem monotonous in nature? Yes.
#
# Convert to SBA: Problem <--- using predicate function ---> SBA
#
# Define the predicate function:
# For the array 12345555678, to find the first occurrence of X:
#
# Convert to binary: 00001111111
# Predicate function: A[i] < X returns 0, otherwise returns 1

# The final check if R < len(arr) and arr[R] == X handles the case you mentioned where X is not in the array but would be inserted at position R.

# O(log n) time complexity

def golden_template_binary_search_last(arr, X):
    def predicate(M):
        if arr[M] <= X:
            return 0
        else:
            return 1

    L = -1
    R = len(arr)

    while L + 1 < R:
        M = (L + R) // 2
        if predicate(M) == 0:
            L = M
        else:
            R = M

    # Handle edge cases and return result
    if L >= 0 and arr[L] == X:
        return L
    else:
        return -1  # X not found in the array

# Test the function
arr = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
X = 5
result = golden_template_binary_search_last(arr, X)
print(f"Last occurrence of {X} is at index: {result}")

# Edge case: X not in array
X = 9
result = golden_template_binary_search_last(arr, X)
print(f"Last occurrence of {X} is at index: {result}")

# This predicate function correctly divides the array into two parts:
# 00000000111
# Where 0 represents elements <= X, and 1 represents elements > X.
