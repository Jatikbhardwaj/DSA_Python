def count_subarrays_with_minimum(A):
    n = len(A)
    left = [0] * n
    right = [0] * n
    stack = []

    # Iterate from left to right
    for i in range(n):
        while stack and A[stack[-1]] > A[i]: # While stack is not empty and the current element is less than the element indexed by the top of the stack
            print("stack: ", stack)
            print(A[stack[-1]] , A[i])
            stack.pop()
        left[i] = stack[-1] + 1 if stack else 0 # Set the left boundary for the current element
        print("left_array: ", left)
        stack.append(i) # Append the current index to the stack

    stack = []

    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        right[i] = stack[-1] - 1 if stack else n - 1
        stack.append(i)

    # Calculate subarray count for each element
    counts = [(i - left[i] + 1) * (right[i] - i + 1) for i in range(n)]

    return counts

# Example usage:
A = [100, 80, 61, 70, 60, 75, 85]
result = count_subarrays_with_minimum(A)
print(result)  # Output: [1, 2, 6, 1, 15, 2, 1]
